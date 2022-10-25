import pytest
from functions import count

def test_count_ones():
    assert count([1,1,1],1)==3

def test_count_nothing():
    assert count([1,1,1],0)==0

def test_count_tests():
    assert count(["test","test", "test"],"test")==3