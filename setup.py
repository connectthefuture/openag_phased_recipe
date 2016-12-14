from os import path
from setuptools import setup, find_packages

readme_path = path.join(path.dirname(__file__), "README.rst")
with open(readme_path) as f:
    readme = f.read()

setup(
    name='openag_phase_recipe',
    version='0.0.1-alpha.1',
    author='Open Agriculture Initiative',
    description='Tools for working with phase-based recipes',
    long_description=readme,
    license="GPL-3.0",
    url="https://github.com/OpenAgInitiative/openag_phase_recipe",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=[
        'pyyaml>=3.12',
        'voluptuous>=0.8.11'
    ],
    extras_require={},
    include_package_data=True,
    entry_points={
        'console_scripts': []
    }
)
