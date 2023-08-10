use crate::alma_values::FieldScanType;
use crate::alma_values::InvertPhaseOptions;
use crate::alma_values::PointingOptions;
use chrono::NaiveDateTime;
use mysql::prelude::*;
use mysql::serde::Deserialize;
use mysql::serde_json;
use mysql::Pool;
use numpy::ndarray::Array2;
use numpy::PyReadonlyArray1;
use numpy::{Complex64, PyArray2};
use std::env::var;
use std::f64::consts::PI;
use std::fs::File;
use std::io::{BufRead, BufReader};

use itertools::izip;
use pyo3::exceptions::PyValueError;
use pyo3::{pyclass, PyCell, PyResult};
use pyo3::{pyfunction, pymethods};

static SPEED_OF_LIGHT: f64 = 299_792_458.0;

#[derive(Deserialize)]
pub struct RawData(f64, f64, f64, f64);

pub fn get_db_url() -> PyResult<String> {
    let env_username = var("DB_USERNAME");
    let env_password = var("DB_PASSWORD");
    let env_hostname = var("DB_HOSTNAME");
    let env_database = var("DB_DATABASE");
    if let Err(_) = env_username {
        return Err(PyValueError::new_err("Missing DB_USERNAME"));
    }
    if let Err(_) = env_password {
        return Err(PyValueError::new_err("Missing DB_PASSWORD"));
    }
    if let Err(_) = env_hostname {
        return Err(PyValueError::new_err("Missing DB_HOSTNAME"));
    }
    if let Err(_) = env_database {
        return Err(PyValueError::new_err("Missing DB_DATABASE"));
    }

    let db_username = env_username.unwrap();
    let db_password = env_password.unwrap();
    let db_hostname = env_hostname.unwrap();
    let db_database = env_database.unwrap();
    Ok(format!(
        "mysql://{}:{}@{}:3306/{}",
        db_username, db_password, db_hostname, db_database
    ))
}

#[pyfunction]
#[pyo3(signature = (keyheader))]
pub fn get_scanset_details(keyheader: i64) -> PyResult<(i64, f64, i64, f64, String)> {
    let url = get_db_url()?;
    let pool = Pool::new(url.as_ref()).unwrap();
    let query = format!(
        "SELECT keyId, f, band, tilt, notes FROM ScanSetDetails WHERE fkHeader={:?}",
        keyheader
    );
    let mut conn = pool.get_conn().unwrap();
    let value = conn
        .query_first::<(i64, f64, i64, f64, String), _>(query)
        .unwrap();

    Ok(value.unwrap())
}

#[pyfunction]
#[pyo3(signature = (keyheader))]
pub fn get_scan_details(
    keyheader: i64,
) -> PyResult<Vec<(i64, i64, i64, f64, NaiveDateTime, i64, i64)>> {
    let url = get_db_url()?;
    let pool = Pool::new(url.as_ref()).unwrap();
    let query = format!(
        "SELECT keyId, sb, pol, ifatten, TS, copol, SourcePosition FROM ScanDetails WHERE fkScanSetDetails={}",
        keyheader
    );
    let mut conn = pool.get_conn().unwrap();

    let values = conn
        .query_map(
            query,
            |val: (i64, i64, i64, f64, NaiveDateTime, i64, i64)| val,
        )
        .unwrap();

    Ok(values)
}

#[pyclass]
#[derive(Clone, Debug, PartialEq, Default)]
pub struct Raster {
    #[pyo3(get, set)]
    key_id: i64,
    #[pyo3(get, set)]
    frequency: f64,
    #[pyo3(get, set)]
    tilt: f64,
    #[pyo3(get, set)]
    band: i32,
    #[pyo3(get, set)]
    timestamp: NaiveDateTime,
    #[pyo3(get, set)]
    pointing_option: PointingOptions,
    #[pyo3(get, set)]
    field_scan: FieldScanType,
    #[pyo3(get, set)]
    invert_phase: bool,

    x_coords: Array2<f64>,
    y_coords: Array2<f64>,
    amp_data: Array2<f64>,
    phase_data: Array2<f64>,

    mask: Array2<f64>,

    ff_az: Array2<f64>,
    ff_el: Array2<f64>,
    ff_amp: Array2<f64>,
    ff_phase: Array2<f64>,

    #[pyo3(get, set)]
    ff_size: usize,
    #[pyo3(get, set)]
    ff_step: f64,

    #[pyo3(get, set)]
    mean_x: f64,
    #[pyo3(get, set)]
    mean_y: f64,
    #[pyo3(get, set)]
    dim_x: usize,
    #[pyo3(get, set)]
    dim_y: usize,
    #[pyo3(get, set)]
    size: usize,
    #[pyo3(get, set)]
    diff_x: f64,
    #[pyo3(get, set)]
    diff_y: f64,
    #[pyo3(get, set)]
    az_nominal: f64,
    #[pyo3(get, set)]
    el_nominal: f64,
}

impl Raster {
    pub fn clear_arrays(&mut self) {
        self.x_coords = Array2::zeros((self.dim_x, self.dim_y));
        self.y_coords = Array2::zeros((self.dim_x, self.dim_y));
        self.amp_data = Array2::zeros((self.dim_x, self.dim_y));
        self.phase_data = Array2::zeros((self.dim_x, self.dim_y));
    }
    pub fn clear_dims(&mut self) {
        self.dim_x = 0;
        self.dim_y = 0;
        self.size = 0;
        self.diff_x = 0.0;
        self.diff_y = 0.0;
    }
    pub fn get_dims(&mut self, data: &RawData, prev: &mut RawData) -> () {
        if data.0 != prev.0 {
            self.diff_x = prev.0 - data.0;
            prev.0 = data.0;
            self.dim_x = 0;
        }
        if data.1 != prev.1 {
            self.diff_y = prev.1 - data.1;
            prev.1 = data.1;
            self.dim_y = 0;
        }
        self.dim_x += 1;
        self.dim_y += 1;
        self.size += 1;
    }
    pub fn store_data(&mut self, res_vec: Vec<RawData>) {
        self.mean_x = 0.0;
        self.mean_y = 0.0;
        self.az_nominal = 0.0;
        self.el_nominal = 0.0;

        let inverted = if !self.field_scan.is_nf() && self.invert_phase {
            -1.0
        } else {
            1.0
        };

        for (it, RawData(x, y, amp, phase)) in res_vec.iter().enumerate() {
            let j = ((it as f64) / (self.dim_x as f64).floor()) as usize;
            let i = it % self.dim_x;
            self.mean_x += inverted * x;
            self.mean_y += inverted * y;
            let linear_amp = 10.0_f64.powf(amp / 20.0);

            *self.x_coords.get_mut((i, j)).unwrap() = inverted * x;
            *self.y_coords.get_mut((i, j)).unwrap() = inverted * y;
            *self.amp_data.get_mut((i, j)).unwrap() = linear_amp;
            *self.phase_data.get_mut((i, j)).unwrap() = inverted * phase * PI / 180.0;
            self.az_nominal += inverted * x * linear_amp * linear_amp;
            self.el_nominal += inverted * y * linear_amp * linear_amp;
        }
        self.mean_x /= self.size as f64;
        self.mean_y /= self.size as f64;
    }
    pub fn adjust_dims(&mut self) {
        if self.dim_x == 1 {
            self.dim_x = self.dim_y;
            self.dim_y = self.size / self.dim_x;
        } else {
            self.dim_y = self.dim_x;
            self.dim_x = self.size / self.dim_y;
        }
    }
    pub fn single_nf2ff(&self, kx_val: f64, ky_val: f64) -> Complex64 {
        let mut im_accu = 0.0;
        let mut re_accu = 0.0;
        for (x_it, y_it, amp_it, phase_it) in izip!(
            &self.x_coords,
            &self.y_coords,
            &self.amp_data,
            &self.phase_data
        ) {
            let diff_x = x_it - self.mean_x;
            let diff_y = y_it - self.mean_y;
            let phase = phase_it + diff_x * kx_val + diff_y * ky_val;
            im_accu += amp_it * phase.cos() * self.diff_x * self.diff_y;
            re_accu += amp_it * phase.sin() * self.diff_x * self.diff_y;
        }
        Complex64::new(im_accu, re_accu)
    }
    pub fn nominal_angles(&mut self) {
        match (self.band, self.pointing_option) {
            // # -- Calculated  --
            (_, PointingOptions::ACTUAL) => (),
            // # -- Band 1 --
            (1, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (1.7553, 1.7553);
            }
            (1, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (2.943499, 2.943499);
            }
            (1, PointingOptions::BAND1TEST) => {
                (self.az_nominal, self.el_nominal) = (0.0, -2.48);
            }
            // # -- Band 2 --
            (2, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (1.7553, -1.7553);
            }
            (2, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (2.898850, -2.898850);
            }
            // # -- Band 3 --
            (3, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (-0.3109, -1.7345);
            }
            (3, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (-0.521949, -2.918507);
            }
            // # -- Band 4 --
            (4, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (-0.3109, 1.7345);
            }
            (4, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (-0.549947, 3.120381);
            }
            // # -- Band 5 --
            (5, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (-1.6867, -1.6867);
            }
            (5, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (-1.874227, -1.874227);
            }
            // # -- Band 6 --
            (6, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (-1.6867, 1.6867);
            }
            (6, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (-1.990572, 1.990572);
            }
            // # -- Band 7 --
            (7, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (-0.9740, 0.0);
            }
            (7, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (-0.764417, 0.0);
            }
            // # -- Band 8 --
            (8, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (0.0, -0.9740);
            }
            (8, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (0.0, -0.757841);
            }
            // # -- Band 9 --
            (9, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (0.0, 0.9740);
            }
            (9, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (0.0, 0.735064);
            }
            // # -- Band 10 --
            (10, PointingOptions::NOMINAL) => {
                (self.az_nominal, self.el_nominal) = (0.9740, 0.0);
            }
            (10, PointingOptions::ACA7METER) => {
                (self.az_nominal, self.el_nominal) = (0.735064, 0.0);
            }
            _ => (),
        }
    }

    pub fn calculate_subreflector_mask(&mut self) {
        let subreflector_radius = self.pointing_option.get_subreflector_radius();

        // Calculate the data meshgrid if necessary
        let step: f64;
        let az_mesh;
        let el_mesh;
        if self.field_scan.is_nf() {
            step = self.ff_step;
            (az_mesh, el_mesh) = (&self.ff_az - self.az_nominal, &self.ff_el - self.el_nominal);
        } else {
            step = (self.diff_x + self.diff_y) / 2.0;
            (az_mesh, el_mesh) = (
                &self.x_coords - self.az_nominal,
                &self.y_coords - self.el_nominal,
            );
        }

        // Radius of the meshgrid with respect the nominal angles
        self.mask = &az_mesh * &az_mesh + &el_mesh * &el_mesh;

        // Calculate inner and outer radius
        let inner_radius = subreflector_radius - step / 2.0;
        let outer_radius = subreflector_radius + step / 2.0;

        for rad_it in self.mask.iter_mut() {
            let rad = rad_it.sqrt();
            if rad < inner_radius {
                *rad_it = 1.0;
            } else if (inner_radius <= rad) && (rad <= outer_radius) {
                *rad_it = (outer_radius - rad) / step;
            } else if rad > outer_radius {
                *rad_it = 0.0
            }
        }
    }
}

#[pymethods]
impl Raster {
    #[new]
    fn new(
        frequency: f64,
        sideband: i64,
        pointing_option: PointingOptions,
        scan_type: FieldScanType,
        invert_phase: InvertPhaseOptions,
    ) -> Self {
        let mut raster = Self::default();
        raster.pointing_option = pointing_option;
        raster.frequency = frequency;
        raster.field_scan = scan_type;
        raster.invert_phase = invert_phase.to_bool(sideband);
        raster
    }

    #[getter]
    fn x_coords<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let x_coords = &this.borrow().x_coords;
        unsafe { PyArray2::borrow_from_array(x_coords, this) }
    }

    #[getter]
    fn y_coords<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let y_coords = &this.borrow().y_coords;
        unsafe { PyArray2::borrow_from_array(y_coords, this) }
    }

    #[getter]
    fn amp_data<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let amp_data = &this.borrow().amp_data;
        unsafe { PyArray2::borrow_from_array(amp_data, this) }
    }

    #[getter]
    fn phase_data<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let phase_data = &this.borrow().phase_data;
        unsafe { PyArray2::borrow_from_array(phase_data, this) }
    }

    #[getter]
    fn mask<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let mask = &this.borrow().mask;
        unsafe { PyArray2::borrow_from_array(mask, this) }
    }

    #[getter]
    fn ff_az<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let ff_az = &this.borrow().ff_az;
        unsafe { PyArray2::borrow_from_array(ff_az, this) }
    }
    #[getter]
    fn ff_el<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let ff_el = &this.borrow().ff_el;
        unsafe { PyArray2::borrow_from_array(ff_el, this) }
    }
    #[getter]
    fn ff_amp<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let ff_amp = &this.borrow().ff_amp;
        unsafe { PyArray2::borrow_from_array(ff_amp, this) }
    }
    #[getter]
    fn ff_phase<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let ff_phase = &this.borrow().ff_phase;
        unsafe { PyArray2::borrow_from_array(ff_phase, this) }
    }

    pub fn get_nearfield_from_file(&mut self, path: &str) -> PyResult<()> {
        self.clear_dims();
        let mut prev = RawData(0.0, 0.0, 0.0, 0.0);

        let f = File::open(path)?;
        let lines = BufReader::new(f).lines();

        let res_vec = lines
            .map(|line| line.unwrap())
            .map(|read_string| -> RawData {
                let words: Vec<&str> = read_string.split_whitespace().collect();
                let unified = "[".to_owned() + &words.join(",") + "]";
                let conv = serde_json::from_str::<RawData>(&unified).unwrap();

                self.get_dims(&conv, &mut prev);
                conv
            })
            .collect();

        self.adjust_dims();
        self.clear_arrays();
        self.store_data(res_vec);
        if self.field_scan.is_ff() {
            self.calculate_subreflector_mask();
            self.nominal_angles();
        };
        Ok(())
    }

    pub fn get_nearfield_from_database(&mut self, keyheader: i64) -> PyResult<()> {
        self.clear_dims();
        let mut prev = RawData(0.0, 0.0, 0.0, 0.0);

        let url = get_db_url()?;
        let pool = Pool::new(url.as_str()).unwrap();
        let mut conn = pool.get_conn().unwrap();
        let table = self.field_scan.scan_string();
        let query = format!(
            "SELECT x, y, amp, phase FROM {} WHERE fkScanDetails={}",
            table, keyheader
        );

        let res_vec = conn
            .query_map(query, |conv: (f64, f64, f64, f64)| {
                let out = RawData(conv.0, conv.1, conv.2, conv.3);

                self.get_dims(&out, &mut prev);
                out
            })
            .unwrap();

        self.adjust_dims();
        self.clear_arrays();
        self.store_data(res_vec);
        if self.field_scan.is_ff() {
            self.calculate_subreflector_mask();
            self.nominal_angles();
        };

        Ok(())
    }

    fn nf2ff<'py>(&mut self) -> PyResult<()> {
        let lambda = SPEED_OF_LIGHT / self.frequency;
        let wave_number = 2.0 * PI / lambda;
        let limit_angle = 15.0;
        let limit_k = limit_angle * PI / 180.0 * wave_number;
        let len = 101;
        let inverted = if self.invert_phase { -1.0 } else { 1.0 };

        self.ff_size = len;
        self.ff_step = limit_angle / (len - 1) as f64;
        self.ff_az = Array2::zeros([len, len]);
        self.ff_el = Array2::zeros([len, len]);
        self.ff_amp = Array2::zeros([len, len]);
        self.ff_phase = Array2::zeros([len, len]);
        self.az_nominal = 0.0;
        self.el_nominal = 0.0;

        let mut amp_normalization = 0.0;
        for j in 0..len {
            let j_frac = j as f64 / (len - 1) as f64;
            let ky_val = 2.0 * limit_k * j_frac - limit_k;
            let el_it = inverted * (2.0 * limit_angle * j_frac - limit_angle);
            for i in 0..len {
                let i_frac = i as f64 / (len - 1) as f64;
                let kx_val = 2.0 * limit_k * i_frac - limit_k;
                let az_it = inverted * (2.0 * limit_angle * i_frac - limit_angle);

                let comp = self.single_nf2ff(kx_val, ky_val);
                amp_normalization += comp.norm() * comp.norm();

                *self.ff_az.get_mut([j, i]).unwrap() = az_it;
                *self.ff_el.get_mut([j, i]).unwrap() = el_it;
                *self.ff_amp.get_mut([j, i]).unwrap() += comp.norm();
                *self.ff_phase.get_mut([j, i]).unwrap() += inverted * comp.arg();
                self.az_nominal += inverted * az_it * comp.norm() * comp.norm();
                self.el_nominal += inverted * el_it * comp.norm() * comp.norm();
            }
        }
        self.az_nominal /= amp_normalization;
        self.el_nominal /= amp_normalization;

        self.calculate_subreflector_mask();
        self.nominal_angles();

        Ok(())
    }
    pub fn calculate_phase_efficiency(
        &self,
        pos: PyReadonlyArray1<f64>,
        angles: Vec<f64>,
    ) -> PyResult<f64> {
        let pos_arr = pos.as_array();
        let (az_mesh, el_mesh);
        let amp_e;
        let phase_e;
        if self.field_scan.is_nf() {
            (az_mesh, el_mesh) = (&self.ff_az, &self.ff_el);
            amp_e = &self.ff_amp;
            phase_e = &self.ff_phase;
        } else {
            (az_mesh, el_mesh) = (&self.x_coords, &self.y_coords);
            amp_e = &self.amp_data;
            phase_e = &self.phase_data;
        }
        let mask = &self.mask;

        // # Offset the angles by using the nominal angles
        let az_array = (az_mesh - angles[0]) * PI / 180.0;
        let el_array = (el_mesh - angles[1]) * PI / 180.0;

        let mut den_int = 0.0;
        let mut re_accu = 0.0;
        let mut im_accu = 0.0;
        for (az_val, el_val, phase_val, amp_val, mask_val) in
            izip!(az_array, el_array, phase_e, amp_e, mask)
        {
            // # Calculate the phase for the current position
            let phase_fit = pos_arr[0] * az_val.sin() * el_val.cos()
                + pos_arr[1] * el_val.sin()
                + pos_arr[2] * az_val.cos() * el_val.cos();
            // # Calculate the phase difference
            let phase_error = phase_val + phase_fit;
            // # Mask the amplitude using the subreflector mask
            let mask_e = amp_val * mask_val;
            re_accu += mask_e * phase_error.cos();
            im_accu += mask_e * phase_error.sin();
            den_int += mask_e;
        }

        // # Calculate the numerator and denominator integrals
        let num_int = (re_accu * re_accu + im_accu * im_accu).sqrt();

        // # Phase efficiency
        let eta_phase = (num_int * num_int) / (den_int * den_int);
        Ok(1.0 - eta_phase)
    }
}
