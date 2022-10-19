import pytest

def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels

def test_count_ones():
    assert count([1,1,1],1)==3

def test_count_nothing():
    assert count([1,1,1],0)==0

def test_count_tests():
    assert count(["test","test", "test"],"test")==3

def test_fact_0():
    assert fact(0)==1

def test_fact_1():
    assert fact(1)==1

def test_fact_10():
    assert fact(10)==3628800

def test_list_of_squares_1():
    assert list_of_squares(1)=={1:1}

def test_list_of_squares_10():
    assert list_of_squares(10)=={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

def test_vowels_spoon():
    assert vowels("spoon")==2

def test_vowels_aeiouu():
    assert vowels("aeiou")==5