import pytest
from tax import getIncomeTaxComplex

def test_getIncomeTaxComplex_no_tax_0():
    assert getIncomeTaxComplex(0)==0

def test_getIncomeTaxComplex_no_tax_11850():
    assert getIncomeTaxComplex(11850)==11850

def test_getIncomeTaxComplex_basic_Rate():
    assert getIncomeTaxComplex(34500)==29970.0

def test_getIncomeTaxComplex_higher_Rate():
    assert getIncomeTaxComplex(150000)==106200.0

def test_getIncomeTaxComplex_highest_Rate():
    assert getIncomeTaxComplex(200000)==228230.0