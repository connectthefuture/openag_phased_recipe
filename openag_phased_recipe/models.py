"""
Schemas for phase-based recipe data.
"""
from voluptuous import Schema, Optional, Required
from voluptuous.validators import Coerce
from env_vars import (
    AIR_TEMPERATURE,
    AIR_HUMIDITY,
    AIR_CARBON_DIOXIDE,
    WATER_POTENTIAL_HYDROGEN,
    WATER_ELECTRICAL_CONDUCTIVITY,
    LIGHT_INTENSITY_RED,
    LIGHT_INTENSITY_BLUE,
    LIGHT_INTENSITY_WHITE
)

def as_bounded_percent(x):
    """Validate and coerce x into a bounded percentage between 0.0..100.0"""
    x = float(x)
    if x < 0 or x > 100:
        raise ValueError("Percent value {} is out of bounds".format(x))
    return x

coerce_float = Coerce(float)
coerce_int = Coerce(int)

Phase = Schema({
    Required("hours", default=12.0): coerce_float, # Number of hours
    Optional(AIR_TEMPERATURE): coerce_float, # Celcius
    Optional(AIR_HUMIDITY): as_bounded_percent, # % Relative
    Optional(AIR_CARBON_DIOXIDE): coerce_float, # PPM
    Optional(WATER_POTENTIAL_HYDROGEN): coerce_float, # PPM
    Optional(WATER_ELECTRICAL_CONDUCTIVITY): coerce_float, # PPM
    Optional(LIGHT_INTENSITY_RED): coerce_float, # PAR
    Optional(LIGHT_INTENSITY_BLUE): coerce_float, # PAR
    Optional(LIGHT_INTENSITY_WHITE): coerce_float, # PAR
})
Phase.__doc__ = """A phase in a recipe."""


Stage = Schema({
    Required("name", default="Untitled"): str, # Name of phase
    Required("days"): coerce_float, # Number of days
    Required("day"): Phase,
    Required("night"): Phase
})
Stage.__doc__ = """
A stage that contains a day and night phase. Day and night will be alternated
until `days` is complete.
"""


PhasedRecipe = Schema({
    Required("recipe_name", default="Untitled"): str,
    Required("recipe_format"): str,
    Required("version"): str,
    Optional("optimization"): [str],
    Optional("date_created"): Coerce(str),
    Optional("author"): str,
    Optional("author_id"): coerce_int,
    Optional("recipe_id"): coerce_int,
    Required("stages"): [Stage]
})
PhasedRecipe.__doc__ = """Phase-based recipe"""


Operation = Schema([coerce_float, str, coerce_float])
Operation.__doc__ = "An single operation in a time series recipe"