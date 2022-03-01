class Student:

    def __init__(self, name, roll_no, gender):
        self.name = name
        self.roll_no = roll_no
        self.gender = gender

    def taking_test(self):
        print("Name : {}, Roll No : {} is taking test".format(self.name, self.roll_no))


class Teacher:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience


if __name__ == "__main__":
    student1 = Student("Vamshi", 10, "M")
    student2 = Student("Utkarsh", 11, "M")
    teacher1 = Teacher("Kallol", 7)
    type(student1)










