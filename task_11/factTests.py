import pytest
from functions import fact

def test_fact_0():
    assert fact(0)==1

def test_fact_1():
    assert fact(1)==1

def test_fact_10():
    assert fact(10)==3628800