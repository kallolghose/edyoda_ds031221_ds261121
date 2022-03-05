from datetime import date

"""
Reference Links : https://www.geeksforgeeks.org/class-method-vs-static-method-python/#:~:text=A%20class%20method%20takes%20cls,nothing%20about%20the%20class%20state.

1. Person Class with attributes name and age
2. One should be able to create an Object by calculating the age from birth year
  - Class Method
"""
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print("Name {}, Age {}".format(self.__name, self.__age))

    @classmethod
    def from_year_of_birth(cls, name, year_of_birth):
        age = date.today().year - year_of_birth
        return cls(name, age)


person = Person.from_year_of_birth("Kallol", 1991)
person.display_info()
