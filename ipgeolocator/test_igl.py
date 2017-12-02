import pytest
import ipgeolocator

def func(x):
    return x + 2

def test_func():
    assert func(4) == 6

def test_isvalid():
    print(ipgeolocator.is_valid(4))
    assert (ipgeolocator.is_valid(3) == 6)
