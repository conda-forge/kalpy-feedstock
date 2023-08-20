#!/bin/bash
set -ex

export CXXFLAGS="${CXXFLAGS} -D_LIBCPP_DISABLE_AVAILABILITY"
export CONDA_ROOT=$PREFIX
$PYTHON -m pip install . --no-deps -vv
