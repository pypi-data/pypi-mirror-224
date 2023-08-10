mod alma_values;
mod raster;

use alma_values::{get_antenna_parameters, FieldScanType, InvertPhaseOptions, PointingOptions};
use pyo3::prelude::*;
use pyo3::{pymodule, types::PyModule, PyResult, Python};
use raster::{get_scan_details, get_scanset_details, Raster};

#[pymodule]
fn nf2ff(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_scan_details, m)?)?;
    m.add_function(wrap_pyfunction!(get_scanset_details, m)?)?;
    m.add_function(wrap_pyfunction!(get_antenna_parameters, m)?)?;
    m.add_class::<FieldScanType>()?;
    m.add_class::<InvertPhaseOptions>()?;
    m.add_class::<PointingOptions>()?;
    m.add_class::<Raster>()?;

    Ok(())
}
