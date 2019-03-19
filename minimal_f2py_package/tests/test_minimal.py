from __future__ import division
import numpy as np
import minimal_f2py_package
import pytest

def test_zadd():
    assert minimal_f2py_package.add.zadd(3.,4.) == np.array([7.+0.j])
