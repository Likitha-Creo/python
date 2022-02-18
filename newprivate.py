class Base:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def funname(self):
        print(self.name)
    def __funage(self):
        print(self.__age)
    def fun(self):
        self.funname()
        self.__funage()

o = Base("likku", 20)
o.fun()
