from math import sqrt

from pyparsing import line

def is_prime(n):
    _prime = True
    if n > 1:
        for i in range(2, int(n/2) + 1):
            if n % i == 0:
                _prime = False
                break
    return _prime


def read_file(f_name):
    f = None
    try:
        f = open(f_name, "r")
        lines = f.readlines()
        print(lines)
    except IOError:
        print("[ERROR] File Not Found")
    finally:
        f.close()

read_file("asdsad.txt")