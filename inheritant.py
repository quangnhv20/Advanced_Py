class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def GetName(self):
        print("I am " + self.name)

class Student(Person):
    def __init__(self, stdName, stdAge, stdYear):
        super().__init__(stdName, stdAge)
        self.stdYear = stdYear

    def welcome(self):
        print("Welcome", self.name, "to the class of", self.stdYear)

std1 = Student("Quang", 23, 4)
std1.welcome()
