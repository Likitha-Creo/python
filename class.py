class Likku:
   alias = "sathya"
   def __init__(self, name, age): 
     self.name = name
     self.age = age
   def fun(self):
     print("my name is", self.name)


obj = Likku("likitha", 20)
obj.fun()
print(obj.alias)
print(obj.name)
