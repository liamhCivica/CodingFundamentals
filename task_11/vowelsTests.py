import pytest
from functions import vowels

def test_vowels_spoon():
    assert vowels("spoon")==2

def test_vowels_aeiouu():
    assert vowels("aeiou")==5