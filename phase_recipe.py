"""
Tools for working with phase-based recipes.
"""
from yaml import load as loads_yaml
from json import dumps as dumps_json
from .models import Recipe


def load_recipe(file_path):
    """Given a YAML file path, load and validate that file"""
    with open(file_path, 'r') as f:
        return Recipe(loads_yaml(f))


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
        "_id": phase_recipe["recipe_id"]
    }


def step_timeseries(state, stage):
    elapsed, series = state
    raise NotImplementedError("TODO")


def to_timeseries_recipe(phase_recipe):
    elapsed, operations = reduce(step_timeseries, phase_recipe["stages"], 0)
    meta = read_phase_meta(phase_recipe)
    timeseries_recipe = ({
        "format": "simple",
        "version": "1.0",
        "operations": operations
    }).append(meta)
    return timeseries_recipe


def map_yaml_to_json(f, yaml_str, *extra):
    """
    Map YAML string to JSON through function.
    yaml str -> json_str
    """
    return dumps_json(f(loads_yaml(yaml_str), *extra))