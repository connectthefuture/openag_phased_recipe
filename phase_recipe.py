"""
Tools for working with phase-based recipes.
"""
from yaml import load as loads_yaml
from json import dumps as dumps_json
from .models import Recipe


def read_phase_meta(phase_recipe):
    """
    Read relevant metadata for recipe that does not change across
    recipe formats
    """
    return {
        "recipe_name": phase_recipe["recipe_name"],
        "date_created": phase_recipe["date_created"],
        "author": phase_recipe["author"],
        "author_id": phase_recipe["author_id"],
        "recipe_id": phase_recipe["recipe_id"]
    }


def to_timeseries_recipe(phase_recipe):
    meta = read_phase_meta(phase_recipe)
    return {
        "recipe_name": phase_desc["recipe_name"],
        "recipe_format": "simple",
        "version": "1.0",
        "date_created": phase_desc[""]
    }


def map_yaml_to_json(f, yaml_str, *extra):
    """
    Map YAML string to JSON through function.
    yaml str -> json_str
    """
    return dumps_json(f(loads_yaml(yaml_str), *extra))