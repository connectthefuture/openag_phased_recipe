"""
Schemas for phase-based recipe data.
"""
from voluptuous import Schema, Optional, Required, validators


def bounded_percent(x):
    """Validate and coerce x into a bounded percentage between 0.0..100.0"""
    x = float(x)
    if x < 0 or x > 100:
        raise ValueError("Percent value {} is out of bounds".format(x))
    return x


Phase = Schema({
    Required("hours", default=12.0): float, # Number of hours
    Optional("air_temperature"): float, # Celcius
    Optional("humidity"): bounded_percent, # % Relative
    Optional("co2"): float, # PPM
    Optional("ph"): float, # PPM
    Optional("red_light"): float, # PAR
    Optional("blue_light"): float, # PAR
    Optional("white_light"): float, # PAR
})
Phase.__doc__ = """A phase in a recipe."""


Stage = Schema({
    "days": float, # Number of days
    "day": Phase,
    "night": Phase
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
    Optional("date_created"): validators.Date,
    Optional("author"): str,
    Optional("author_id"): int,
    Optional("recipe_id"): int,
    Required("stages"): [Stage]
})
Recipe.__doc__ = """Phase-based recipe"""