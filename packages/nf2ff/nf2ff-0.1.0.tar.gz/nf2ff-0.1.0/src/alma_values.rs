use pyo3::prelude::*;

#[pyclass]
#[derive(Clone, Debug, PartialEq, Default)]
#[allow(non_camel_case_types)]
pub enum FieldScanType {
    #[default]
    NEAR_FIELD = 0,
    FAR_FIELD = 1,
}

#[pymethods]
impl FieldScanType {
    pub fn scan_string(&self) -> &str {
        match self {
            FieldScanType::NEAR_FIELD => "BeamListings_nearfield",
            _ => "BeamListings_farfield",
        }
    }
    pub fn __str__(&self) -> &str {
        match self {
            FieldScanType::NEAR_FIELD => "near",
            _ => "far",
        }
    }
    pub fn is_nf(&self) -> bool {
        match self {
            FieldScanType::NEAR_FIELD => true,
            _ => false,
        }
    }
    pub fn is_ff(&self) -> bool {
        match self {
            FieldScanType::NEAR_FIELD => false,
            _ => true,
        }
    }
}

#[pyclass]
#[derive(Clone, Copy, Debug, PartialEq, Default)]
#[allow(non_camel_case_types)]
pub enum PointingOptions {
    //"""PointingOptions Enum"""
    #[default]
    NOMINAL = 0,
    ACTUAL = 1,
    ACA7METER = 2,
    BAND1TEST = 3,
    REDUCE_SUB = 4,
}

impl PointingOptions {
    pub fn get_subreflector_radius(&self) -> f64 {
        let subreflector_radius12m = 3.57633437;
        let subreflector_radius7m = 3.5798212165;
        let subreflector_reduced = 2.0;

        match self {
            PointingOptions::ACA7METER => subreflector_radius7m,
            PointingOptions::REDUCE_SUB => subreflector_reduced,
            _ => subreflector_radius12m,
        }
    }
}

#[pyclass]
#[derive(Clone, Debug, PartialEq, Default)]
#[allow(non_camel_case_types)]
pub enum InvertPhaseOptions {
    //"""InvertPhaseOptions Enum"""
    #[default]
    INVERT_LSB,
    INVERT_USB,
    INVERT_ALL,
    INVERT_NONE,
}

impl InvertPhaseOptions {
    pub fn to_bool(&self, sideband: i64) -> bool {
        match self {
            InvertPhaseOptions::INVERT_USB => sideband == 1,
            InvertPhaseOptions::INVERT_LSB => sideband == 2,
            InvertPhaseOptions::INVERT_ALL => true,
            InvertPhaseOptions::INVERT_NONE => false,
        }
    }
}

#[pyclass]
#[derive(Clone, Debug, PartialEq, Default)]
pub struct AntennaParameters {
    //"""AntennaParameters Enum"""
    //"""Contains the parameters for the different types of ALMA antennas"""
    #[pyo3(get, set)]
    plate_factor: f64,
    #[pyo3(get, set)]
    dish_diameter: f64,
}

#[pyfunction]
pub fn get_antenna_parameters(pointing: PointingOptions) -> AntennaParameters {
    // """Returns the parameters for a given antenna pointing option

    // Args:
    //     pointing (PointingOptions, optional): Pointing option used for calculation. Defaults to PointingOptions.NOMINAL.

    // Returns:
    //     AntennaParameters: Antenna parameters for the selected pointing option
    // """
    match pointing {
        PointingOptions::ACA7METER => AntennaParameters {
            plate_factor: 3.6833,
            dish_diameter: 7.0,
        },
        _ => AntennaParameters {
            plate_factor: 2.148,
            dish_diameter: 12.0,
        },
    }
}
