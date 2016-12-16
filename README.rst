openag_phased_recipe
====================

Tools for working with phased climate recipes. See "fixtures" directory for
examples.

Use
---

Once installed, you can use the command line utility to convert from phased
recipe files to JSON timeseries recipes::

    openag_phased_to_timeseries fixtures/test.yaml --out_file test.json


Install
-------

Requirements:

- Python 2.7+

Install with pip::

    git clone https://github.com/OpenAgInitiative/openag_phased_recipe.git
    cd openag_phased_recipe
    pip install -e .