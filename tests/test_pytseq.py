"""Tests: Quantum circuits.
"""
import pytest
import numpy as np
from pytseg.seg import normalize, cut, segment_stationarity
    
def test_dummy():
    pass

def test_normalize(N=1000, seed=42):
    x = np.random.RandomState(seed).rand(N)
    t = np.arange(x.size)
    x, t = normalize(x, t)
    assert x.shape == t.shape
    assert np.all(t[:-1] < t[1:])

def test_cut_rnd(N=1000, seed=42):
    x = np.random.RandomState(seed).rand(N)
    s = cut(x)
    assert s.size <= x.size-1

def test_stationarity_const(c=0, N=100, threshold=.01):
    x = np.ones(N) * c
    s = cut(x)
    l = segment_stationarity(x, s, threshold=threshold)
    assert s.size == 0
    assert np.all(l)
    
