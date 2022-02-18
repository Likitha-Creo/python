class Base:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def funname(self):
        print(self.name)
    def __funage(self):
        print(self.__age)

class Derived(Base):
    def __init__(self, name, age, addr):
        Base.__init__(self, name, age)
        self.addr = addr
    def child(self):
        self.funname()       
        print(self.addr)
        self.__funage()

obj1 = Base("likku", 20)

obj1.funname()
obj1._Base__funage()

obj2 = Derived("likku", 20, "tirupati")
obj2.child()
       
