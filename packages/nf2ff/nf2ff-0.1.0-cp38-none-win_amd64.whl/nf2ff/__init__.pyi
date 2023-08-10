from enum import IntEnum
from datetime import datetime
from typing import Any
import numpy as np
from numpy.typing import NDArray

class AntennaParameters:
    plate_factor: float
    dish_diameter: float

class FieldScanType(IntEnum):
    NEAR_FIELD: int
    FAR_FIELD: int
    def is_nf(self) -> bool: ...
    def is_ff(self) -> bool: ...
    def __str__(self) -> str: ...

class PointingOptions(IntEnum):
    NOMINAL: int
    ACTUAL: int
    ACA7METER: int
    BAND1TEST: int
    REDUCE_SUB: int

class InvertPhaseOptions(IntEnum):
    INVERT_LSB: int
    INVERT_USB: int
    INVERT_ALL: int
    INVERT_NONE: int

class Raster:
    x_coords: NDArray[np.float64]
    """For near-field data contains the X position in meters.\n
    For far-field data contains the azimuth angle in degrees."""
    y_coords: NDArray[np.float64]
    """For near-field data contains the Y position in meters.\n
    For far-field data contains the elevation angle in degrees."""
    data_step: float | np.floating[Any]
    """For near-field is the step in X and Y in meters.\n
    For far-field is the step in azimuth and elevation in degrees."""
    amp_data: NDArray[np.float64]
    """Contains amplitude data in linear magnitude."""
    phase_data: NDArray[np.float64]
    """Contains phase data in radians."""
    mask: NDArray[np.float64]
    """Contains a mask for the antenna secondary."""
    ff_amp: NDArray[np.float64]
    """`Near-field only`. Contains amplitude data in linear magnitude for far-field transformation."""
    ff_phase: NDArray[np.float64]
    """`Near-field only`. Contains phase data in radians for far-field transformation."""
    ff_az: NDArray[np.float64]
    """`Near-field only`. Contains the azimuth angle in degrees for far-field transformation."""
    ff_el: NDArray[np.float64]
    """`Near-field only`. Contains the elevation angle in degrees for far-field transformation."""
    ff_size: int
    """`Near-field only`. Number of points per axis for far-field transformation."""
    ff_limit: float
    """`Near-field only`. Limit in degrees for the angles for far-field transformation."""
    ff_step: float
    """`Near-field only`. Angle step for azimuth and elevation in degrees."""
    az_nominal: float | np.floating[Any]
    """Nominal azimuth angle used for calculation.\n
    In degrees."""
    el_nominal: float | np.floating[Any]
    """Nominal elevation angle used for calculation.\n
    In degrees."""
    frequency: float

    dim_x: int
    dim_y: int

    field_scan: FieldScanType
    """FieldScanType of this raster: Near-Field or Far-Field"""
    pointing_option: PointingOptions
    """PointingOption used for calculation"""
    def __init__(
        self,
        frequency: float,
        sideband: int,
        pointing_option: PointingOptions,
        scan_type: FieldScanType,
        invert_phase: InvertPhaseOptions,
    ): ...
    def nf2ff(self) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
    def asdf(self): ...
    def get_nearfield_from_database(self, keyheader: int): ...
    def get_nearfield_from_file(self, path: str | int): ...
    def calculate_phase_efficiency(
        self, pos: NDArray[np.float64], angles: list[float | np.floating[Any]]
    ) -> float: ...

def get_scanset_details(
    keyheader: int,
) -> tuple[int, float, int, float, str]: ...
def get_scan_details(
    keyheader: int,
) -> list[tuple[int, int, int, float, datetime, int, int]]: ...
def get_antenna_parameters(
    pointing: PointingOptions = PointingOptions.NOMINAL,
) -> AntennaParameters: ...
