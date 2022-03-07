from oops_day1 import my_programs
import pytest

"""
File name of unitest test case should always start with
test

Unit test cases are user defined functions
Unit test case should always start with test
"""

def test_basic():
    assert True

@pytest.mark.parametrize(
                        "ip1, ip2, output",
                         [
                             (10, 10, 20),
                             (101, 101, 202),
                             (1000, 1000, 2000)
                          ]
                         )
def test_params(ip1, ip2, output):
    actual_output = my_programs.sum(ip1, ip2)
    assert actual_output == output

@pytest.mark.parametrize(
                        "ip1, ip2, output",
                         [
                             (10, 10, 20),
                             (101, 101, 202),
                             (1000, 1000, 2000)
                          ]
                         )
def test_params2(ip1, ip2, output):
    actual_output = my_programs.sum(ip1, ip2)
    assert actual_output == output


