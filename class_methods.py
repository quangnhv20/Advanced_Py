class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def GetName(self):
        print("Hello I am " + self.name)

p1 = Person('quang', 23)
p1.GetName()

