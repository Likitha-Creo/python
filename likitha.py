class Person:
   def __init__(self):
       self.name = "likitha"
       self._age = 20
       self.__addr = "tirupati"

p = Person()
p._person__addr = "kurnool"
print(p._person__addr)
