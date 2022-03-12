from programs import programs
import pytest

def test_basic():
    assert True

def test_passes_without_info():
    with pytest.raises(Exception):
        x = 1 / 0

def test_isprime():
    assert programs.is_prime(3)

def test_is_not_prime():
    assert not programs.is_prime(10)