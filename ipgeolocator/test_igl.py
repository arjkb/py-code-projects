import pytest
import ipgeolocator

def func(x):
    return x + 2

def test_func():
    assert func(4) == 6

def test_isvalid():
    assert (ipgeolocator.is_valid('192.168.4.5') == True)
    assert (ipgeolocator.is_valid('0.0.0.0') == True)
    assert (ipgeolocator.is_valid('255.255.255.255') == True)

    assert (ipgeolocator.is_valid('0.0.0.256') == False)
    assert (ipgeolocator.is_valid('0.0.256.0') == False)
    assert (ipgeolocator.is_valid('0.256.0.0') == False)
    assert (ipgeolocator.is_valid('256.0.0.0') == False)
    assert (ipgeolocator.is_valid('100.200.300.400') == False)

    assert (ipgeolocator.is_valid('256.256.256.256') == False)
    assert (ipgeolocator.is_valid('-1,-1,-1,-1') == False)
    assert (ipgeolocator.is_valid('192.168') == False)
