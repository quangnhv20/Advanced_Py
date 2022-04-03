class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
yname = input("What is your name? ")
yage = input("how old are you? ")
person1 = person(yname,yage)
 
print(person1.name)
print(person1.age)
