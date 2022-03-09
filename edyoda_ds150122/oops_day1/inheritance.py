class Parent:

    def __init__(self, name):
        self.name = name


class Son(Parent):

    def __init__(self, name, education):
        super(Son, self).__init__(name)
        self.education = education