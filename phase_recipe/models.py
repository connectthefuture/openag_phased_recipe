"""
Schemas for phase-based recipe data.
"""
from voluptuous import Schema, Optional, Required, validators
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

def bounded_percent(x):
    """Validate and coerce x into a bounded percentage between 0.0..100.0"""
    x = float(x)
    if x < 0 or x > 100:
        raise ValueError("Percent value {} is out of bounds".format(x))
    return x


Phase = Schema({
    Required("hours", default=12.0): float, # Number of hours
    Optional(AIR_TEMPERATURE): float, # Celcius
    Optional(AIR_HUMIDITY): bounded_percent, # % Relative
    Optional(AIR_CARBON_DIOXIDE): float, # PPM
    Optional(WATER_POTENTIAL_HYDROGEN): float, # PPM
    Optional(WATER_ELECTRICAL_CONDUCTIVITY): float, # PPM
    Optional(LIGHT_INTENSITY_RED): float, # PAR
    Optional(LIGHT_INTENSITY_BLUE): float, # PAR
    Optional(LIGHT_INTENSITY_WHITE): float, # PAR
})
Phase.__doc__ = """A phase in a recipe."""


Stage = Schema({
    Required("name", default="Untitled"): str, # Name of phase
    Required("days"): float, # Number of days
    Required("day"): Phase,
    Required("night"): Phase
})
Stage.__doc__ = """
A stage that contains a day and night phase. Day and night will be alternated
until `days` is complete.
"""


Recipe = Schema({
    Required("recipe_name", default="Untitled"): str,
    Required("recipe_format"): str,
    Required("version"): str,
    Optional("optimization"): [str],
    Optional("date_created"): validators.Datetime,
    Optional("author"): str,
    Optional("author_id"): int,
    Optional("recipe_id"): int,
    Required("stages"): [Stage]
})
Recipe.__doc__ = """Phase-based recipe"""


Operation = Schema([float, str, float])
Operation.__doc__ = "An single operation in a time series recipe"