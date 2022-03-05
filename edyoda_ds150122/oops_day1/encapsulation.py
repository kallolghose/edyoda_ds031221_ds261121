# Private attributes : cannot be updated outside the class
# it is marked by _ or __ at the beginning of the attribute
# getters and setters
class Teacher:

    def __init__(self, name):
        self.__name = name

    def evaluating(self):
        print("Teacher {} is evaluating".format(self.__name))

    # Getter : used to get the value of the private attribute
    # Getter naming convention : get_attribute_name
    def get_name(self):
        return self.__name

    # Setter : used to set/update the value of the private attribute
    # Setter naming convention : set_attribute_name
    def set_name(self, value):
        self.__name = value


# How to create object
# variableName = Class_Name(<Number of parameters in __init__ without self>)
teacher1 = Teacher("kallol")
teacher1.evaluating()
print("Name of teacher for object teacher1 = {}".format(teacher1.get_name()))
teacher1.set_name("Mayank") # this will change the value of private attribute __name = Mayank
print("Updated Name of teacher for object teacher1 = {}".format(teacher1.get_name()))



