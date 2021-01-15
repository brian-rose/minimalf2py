from __future__ import division
import numpy as np
import minimalf2py
import pytest

def test_zadd():
    assert minimalf2py.add.zadd(3.,4.) == np.array([7.+0.j])
