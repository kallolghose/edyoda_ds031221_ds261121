from my_programs.all_programs import is_prime
import pytest


@pytest.mark.parametrize("num", [1, 2, 3, 5, 11])
def test_is_prime(num):
    assert is_prime(num)

@pytest.mark.parametrize("num", [10, 12, 20, 30])
def test_is_not_prime(num):
    actual = is_prime(num)
    assert actual == False



