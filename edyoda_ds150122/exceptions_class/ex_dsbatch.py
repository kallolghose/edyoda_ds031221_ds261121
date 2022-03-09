def validate_age(age):
    if age < 0:
        # Exception is being raised
        raise ValueError("Age Cannot be less than Zero")
    print("Age {} is valid".format(age))


# Exception is being handled

try:
    fp = open("C:/Users/Hp/OneDrive/Documents/workspace/edYoda/python_space/test_code/index.txt", "a")
    lines = fp.write("Kallol")
    print(lines)
except ValueError:
    print("[ERROR] There is some exception")
finally:
    print("============== Close the file !! ========================")

print("This will not be executed if the exeception is raised")
