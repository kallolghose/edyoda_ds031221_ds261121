"""
Celsius to Fahrenheit
Formula : F = 1.8 * C + 32
Create a class Celsius which has a attribute called temperature and behaviour to_fahrenheit()
Behaviour to_fahrenheit() will convert the temperature from C to F

2. Use encapsulation and getters and setters
3. Check value of temperature > -273.15
    if temp < -273.15 print an error message and set temp to 0

Link : Getters Setters : https://www.programiz.com/python-programming/property
"""
class Celsius:

    def __init__(self, temperature):
        # self.__temperature = temperature
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return 1.8 * self.__temperature + 32

    def get_temperature(self):
        return self.__temperature

    # If you want to perform conditional checks on attributes setters comes in handy
    def set_temperature(self, value):
        if value < -273.15:
            print("[ERROR] temperature should be greater than -273.15")
            self.__temperature = 0
            return
        self.__temperature = value


cel = Celsius(-1500) # Creating object
print("{} C = {} F".format(cel.get_temperature(), cel.to_fahrenheit()))
cel.set_temperature(100) # updating the temperature attribute
print("{} C = {} F".format(cel.get_temperature(), cel.to_fahrenheit()))
cel.set_temperature(150)
print("{} C = {} F".format(cel.get_temperature(), cel.to_fahrenheit()))
cel.set_temperature(-1500)