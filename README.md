# minimalf2py

[![Build and test](https://github.com/brian-rose/minimalf2py/actions/workflows/build-and-test.yaml/badge.svg)](https://github.com/brian-rose/minimalf2py/actions/workflows/build-and-test.yaml) [![Conda build](https://github.com/brian-rose/minimalf2py/actions/workflows/conda-build.yaml/badge.svg)](https://github.com/brian-rose/minimalf2py/actions/workflows/conda-build.yaml)

A minimal package to diagnose issues with building Python / Fortran packages with f2py

Also a useful working example of how to use GitHub Actions to build this kind of package for Linux, MacOs, and Windows.

[Brian E. J. Rose](https://brian-rose.github.io)

## Building from source

### Build environment

Here are instructions to create a build environment (including Fortran compiler) with conda/mamba

Starting from the root of the `minimalf2py` repo:
```
mamba env create --file environment.yml
conda activate minimal_build_env
```

### Building and installing into the Python environment

From the root of the repository, do this:
```
python -m pip install . --no-deps -vv
```

### Running tests

To run tests, do this from any directory other than the minimalf2py repo:
```
pytest -v --pyargs minimalf2py
```
