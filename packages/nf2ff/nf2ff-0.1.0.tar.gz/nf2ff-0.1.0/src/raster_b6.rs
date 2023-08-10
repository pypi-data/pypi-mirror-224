use chrono::NaiveDateTime;
use mysql::prelude::*;
use mysql::*;
use numpy::ndarray::Array2;
use numpy::{Complex64, PyArray2};
use serde::Deserialize;
use std::env::var;
use std::f64::consts::PI;

use itertools::izip;

use crate::alma_values::PointingOptions;

use pyo3::exceptions::PyValueError;
use pyo3::{pyclass, pyfunction, pymethods, PyCell, PyResult};

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
pub fn get_scanset_details_b6(keyheader: i64) -> PyResult<(i64, f64)> {
    let url = get_db_url()?;
    let pool = Pool::new(url.as_ref()).unwrap();
    let query = format!(
        "SELECT keyBeamPattern, FreqCarrier FROM BeamPatterns WHERE keyBeamPattern={}",
        keyheader
    );
    let mut conn = pool.get_conn().unwrap();
    let value = conn.query_first::<(i64, f64), _>(query).unwrap().unwrap();

    Ok(value)
}

#[pyfunction]
#[pyo3(signature = (keyheader))]
pub fn get_scan_details_b6(
    keyheader: i64,
) -> PyResult<Vec<(i64, i64, i64, f64, NaiveDateTime, i64, i64)>> {
    let url = get_db_url()?;
    let pool = Pool::new(url.as_ref()).unwrap();
    let query = format!(
        "SELECT keyBeamPattern, sb, pol, ifatten, TS, copol, SourcePosition FROM BeamPatterns WHERE keyBeamPattern={}",
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
pub struct RasterB6 {
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

    x: Array2<f64>,
    y: Array2<f64>,
    amp: Array2<f64>,
    phase: Array2<f64>,

    ff_az: Array2<f64>,
    ff_el: Array2<f64>,
    ff_amp: Array2<f64>,
    ff_phase: Array2<f64>,
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

impl RasterB6 {
    fn clear_arrays(&mut self) {
        self.x = Array2::zeros((self.dim_x, self.dim_y));
        self.y = Array2::zeros((self.dim_x, self.dim_y));
        self.amp = Array2::zeros((self.dim_x, self.dim_y));
        self.phase = Array2::zeros((self.dim_x, self.dim_y));
    }
    fn clear_dims(&mut self) {
        self.dim_x = 0;
        self.dim_y = 0;
        self.size = 0;
        self.diff_x = 0.0;
        self.diff_y = 0.0;
    }
    fn get_dims(&mut self, data: &RawData, prev: &mut RawData) -> () {
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
    fn store_data(&mut self, res_vec: Vec<RawData>, inverted: f64) {
        self.mean_x = 0.0;
        self.mean_y = 0.0;
        for (it, RawData(x, y, amp, phase)) in res_vec.iter().enumerate() {
            let j = ((it as f64) / (self.dim_x as f64).floor()) as usize;
            let i = it % self.dim_x;
            self.mean_x += inverted * x;
            self.mean_y += inverted * y;

            *self.x.get_mut((i, j)).unwrap() = inverted * x;
            *self.y.get_mut((i, j)).unwrap() = inverted * y;
            *self.amp.get_mut((i, j)).unwrap() = 10.0_f64.powf(amp / 20.0);
            *self.phase.get_mut((i, j)).unwrap() = inverted * phase * PI / 180.0;
        }
        self.mean_x /= self.size as f64;
        self.mean_y /= self.size as f64;
    }
    fn adjust_dims(&mut self) {
        if self.dim_x == 1 {
            self.dim_x = self.dim_y;
            self.dim_y = self.size / self.dim_x;
        } else {
            self.dim_y = self.dim_x;
            self.dim_x = self.size / self.dim_y;
        }
    }
    fn single_nf2ff(&self, kx_val: f64, ky_val: f64) -> Complex64 {
        let mut im_accu = 0.0;
        let mut re_accu = 0.0;
        for (x_it, y_it, amp_it, phase_it) in izip!(&self.x, &self.y, &self.amp, &self.phase) {
            let diff_x = x_it - self.mean_x;
            let diff_y = y_it - self.mean_y;
            let phase = phase_it + diff_x * kx_val + diff_y * ky_val;
            im_accu += amp_it * phase.cos();
            re_accu += amp_it * phase.sin();
        }
        im_accu *= self.diff_x * self.diff_y;
        re_accu *= self.diff_x * self.diff_y;
        Complex64::new(im_accu, re_accu)
    }
}

#[pymethods]
impl RasterB6 {
    #[new]
    fn new(pointing_option: PointingOptions) -> Self {
        let mut raster = Self::default();
        raster.pointing_option = pointing_option;
        raster
    }

    #[getter]
    fn x<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let x = &this.borrow().x;
        unsafe { PyArray2::borrow_from_array(x, this) }
    }

    #[getter]
    fn y<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let y = &this.borrow().y;
        unsafe { PyArray2::borrow_from_array(y, this) }
    }

    #[getter]
    fn amp<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let amp = &this.borrow().amp;
        unsafe { PyArray2::borrow_from_array(amp, this) }
    }

    #[getter]
    fn phase<'py>(this: &'py PyCell<Self>) -> &'py PyArray2<f64> {
        let phase = &this.borrow().phase;
        unsafe { PyArray2::borrow_from_array(phase, this) }
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

    pub fn get_nearfield_from_database(&mut self, keyheader: i64, invert: bool) -> PyResult<()> {
        self.clear_dims();
        let inverted = if invert { -1.0 } else { 1.0 };
        let mut prev = RawData(0.0, 0.0, 0.0, 0.0);

        let url = get_db_url()?;
        let pool = Pool::new(url.as_str()).unwrap();
        let mut conn = pool.get_conn().unwrap();
        let query = format!(
            "SELECT Position_X, Position_Y, Power, Phase FROM BP_Data WHERE fkBeamPattern={}",
            keyheader
        );

        let res_vec = conn
            .query_map(query, |conv: (f64, f64, f64, f64)| {
                let out = RawData(conv.0 / 1000.0, conv.1 / 1000.0, conv.2, conv.3);

                self.get_dims(&out, &mut prev);
                out
            })
            .unwrap();

        self.adjust_dims();
        self.clear_arrays();
        self.store_data(res_vec, inverted);
        Ok(())
    }

    fn nf2ff<'py>(&mut self, invert: bool) -> PyResult<()> {
        let lambda = SPEED_OF_LIGHT / self.frequency;
        let wave_number = 2.0 * PI / lambda;
        let limit_angle = 15.0;
        let limit_k = limit_angle * PI / 180.0 * wave_number;
        let len = 101;
        let inverted = if invert { -1.0 } else { 1.0 };
        self.ff_step = limit_k / (len - 1) as f64;
        self.ff_az = Array2::zeros([len, len]);
        self.ff_el = Array2::zeros([len, len]);
        self.ff_amp = Array2::zeros([len, len]);
        self.ff_phase = Array2::zeros([len, len]);
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
        Ok(())
    }
}
