class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printing(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self, name, age, addr):
        Person.__init__(self, name, age)
        self.addr = addr
    def details(self):
        print(self.name, self.age, self.addr)
    

obj = Student("likku", 20, "tirupati")
obj.details()

