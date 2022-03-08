# val = input("Enter Some Value : ")
# print(val)

# try: except: block to handle the exception
# When the developer wants to decide the course of action in case of an exception
# then the developer handles the exception

try:
    dividend = int(input("Enter Dividend : "))
    divisor = int(input("Enter Divisor : "))
    result = dividend / divisor
    print("Division {}".format(result))
except (ZeroDivisionError, ValueError):
    print("Error while division")
# except ValueError:
#     print("Improper Input Given")

result = 10 + 2
print("Addition {}".format(result))