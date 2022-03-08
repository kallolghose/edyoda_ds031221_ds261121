def validate_age(age):
    if age < 0:
        # Exception is being raised
        raise ValueError("Age Cannot be less than Zero")
    print("Age {} is valid".format(age))


# Exception is being handled
try:
    validate_age(-10)
except ValueError:
    print("[ERROR] There is some exception")