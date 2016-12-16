"""
Tools for working with phase-based recipes.
"""
from yaml import load as loads_yaml
from json import dumps as dumps_json
from models import PhasedRecipe, Operation
from env_vars import VARIABLES


OPERATION_TIMESTEP = 60 # seconds


def read_phase_meta(phased_recipe):
    """
    Read relevant metadata for recipe that does not change across
    recipe formats
    """
    return {
        "recipe_name": phased_recipe["recipe_name"],
        "date_created": phased_recipe["date_created"],
        "author": phased_recipe["author"],
        "author_id": phased_recipe["author_id"],
        "_id": phased_recipe["recipe_id"]
    }


def hrs_to_seconds(hrs):
    return hrs * (60 * 60)


def days_to_seconds(days):
    return hrs_to_seconds(days * 24)


def gen_timestep_operations(timestamp, phase):
    """
    Given a timestamp and a phase model, generate a tuple of operation
    models whos values are the keys in the phase that correspond to
    environmental variables.
    """
    intersection = set.intersection(VARIABLES, set(phase.keys()))
    for key in intersection:
        yield Operation([float(timestamp), key, float(phase[key])])


def gen_phase_operations(elapsed, phase):
    """Expand a phase within a stage into operations"""
    duration = hrs_to_seconds(phase["hours"])
    end_of_phase = elapsed + duration
    while elapsed < end_of_phase:
        elapsed += OPERATION_TIMESTEP
        for operation in gen_timestep_operations(elapsed, phase):
            yield operation


def gen_stage_operations(elapsed, stage):
    duration = days_to_seconds(stage["days"])
    end_of_stage = elapsed + duration
    phases = (stage["day"], stage["night"])
    phase_count = 0
    while elapsed < end_of_stage:
        phase = phases[phase_count % 2]
        phase_count += 1
        for operation in gen_phase_operations(elapsed, phase):
            elapsed = operation[0]
            yield operation


def gen_stages_operations(elapsed, stages):
    for stage in stages:
        for operation in gen_stage_operations(elapsed, stage):
            elapsed = operation[0]
            yield operation


def to_timeseries_recipe(phased_recipe):
    phased_recipe = PhasedRecipe(phased_recipe)
    operations = list(gen_stages_operations(0, phased_recipe["stages"]))
    meta = read_phase_meta(phased_recipe)
    timeseries_recipe = {
        "format": "simple",
        "version": "1.0",
        "operations": operations
    }
    timeseries_recipe.update(meta)
    return timeseries_recipe


def map_yaml_to_json(f, yaml_str, *extra):
    """
    Map YAML string to JSON through function.
    yaml str -> json_str
    """
    return dumps_json(f(loads_yaml(yaml_str), *extra))