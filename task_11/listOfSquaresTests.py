import pytest
from functions import list_of_squares

def test_list_of_squares_1():
    assert list_of_squares(1)=={1:1}

def test_list_of_squares_10():
    assert list_of_squares(10)=={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}