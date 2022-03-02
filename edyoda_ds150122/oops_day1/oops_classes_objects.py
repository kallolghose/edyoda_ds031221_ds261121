class Student:
    # class variable
    classroom = 10

    # Self is a keyword provided by python and its
    # usage is mostly found inside the class body
    # self refer to the objects reference (memory location of the object)
    # self defines the attributes and the behaviours
    def __init__(self, name, roll_no, gender):
        self.name = name # Anything with self is also calles as Instance Variable
        self.roll_no = roll_no
        self.gender = gender

    # Method/Function/Behaviour
    def taking_test(self):
        print("Name : {}, Roll No : {} is taking test".format(self.name, self.roll_no))

# Best way to access a class variable is to use the Class Name
# To access the class variable no need to create an object
print("Classroom {}".format(Student.classroom))

# student1 is an object of Class Student
# student1 is a variable of Type Student
student1 = Student("Vamshi", 10, "M")
student1.name = "Kallol"
print("Name of Student 1 {}".format(student1.name))
print("Student 1 Classroom {}".format(student1.classroom))
# student1-----
# name = Vamshi
# roll_no = 10
# gender = M
# classroom = 10
student2 = Student("Neeraj", 20, "M")
print("Name of Student 2 {}".format(student2.name))
print("Student 2 Classroom {}".format(student2.classroom))
# student2-----
# name = Neeraj
# roll_no = 20
# gender = M
# classroom = 10

# When we call a behavious/function
# student1.taking_test()
# Python will call Student.taking_test(student1)
# where the parameter self is now replaced with student1 (or the calling object)










