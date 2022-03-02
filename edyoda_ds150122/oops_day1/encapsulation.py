# Private attributes : cannot be updated outside the class
# it is marked by _ or __ at the beginning of the attribute
# setters and getters
class Teacher:

    def __init__(self, name):
        self.__name = name

    def evaluating(self):
        print("Teacher {} is evaluating".format(self.__name))


# variableName = Class_Name(<Number of parameters in __init__ without self>)
teacher1 = Teacher("kallol")
teacher1.evaluating()

teacher1 = Teacher("Neerak")
teacher1.evaluating()



