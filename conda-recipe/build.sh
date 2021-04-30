#!/bin/bash

#  Based on conda-forge recipe for scipy
export LIBRARY_PATH="${PREFIX}/lib"
export C_INCLUDE_PATH="${PREFIX}/include"
export CPLUS_INCLUDE_PATH="${PREFIX}/include"

$PYTHON -m pip install . --no-deps -vv
