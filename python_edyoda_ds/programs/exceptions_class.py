from user_defined_exceptions import Networkerror


def perform_division(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError as err:
        print("[ERROR] {}".format(err.args))
    else:
        print("{} / {} = {}".format(dividend, divisor, result))

def raise_user_defined_exception():
    try:
        raise Networkerror("There is a network error")
    except Networkerror as nerr:
        print(nerr.message)


inp = input("Enter Something : ")