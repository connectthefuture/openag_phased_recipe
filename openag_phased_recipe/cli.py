"""Command-line integration for converting phase-based recipes"""
import argparse
from sys import stdin, stdout
from openag_phased_recipe import map_yaml_to_json, to_timeseries_recipe

parser_phased_to_timeseries = argparse.ArgumentParser(
    description="""
    A tool for converting from phased recipes to timeseries recipes.

    Typical use: `openag_phased_to_timeseries my_recipe.yml -o my_recipe.json`
    """,
)
parser_phased_to_timeseries.add_argument(
    'in_file',
    help="A yaml file to read phased climate recipe from. Defaults to stdin.",
    nargs="?",
    type=argparse.FileType('r'),
    default=stdin
)
parser_phased_to_timeseries.add_argument(
    '-o','--out_file',
    help="File to write JSON timeseries recipe to. Defaults to stdout.",
    type=argparse.FileType('w'),
    default=stdout
)

def main():
    args = parser_phased_to_timeseries.parse_args()
    yaml_str = args.in_file.read()
    json_str = map_yaml_to_json(to_timeseries_recipe, yaml_str)
    args.out_file.write(json_str)

if __name__ == '__main__':
    main()