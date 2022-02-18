l = [1, 2, 3, 4]
t = (5, 6, 7, 8)
l.append(10)
l.extend(t)
l.insert(2, 9)
l.remove(4)
print(l.pop())
l.append(1)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
l.copy()
print(l)
print(l.index(7))
del l[2]
print(l)
del l[0:5]
print(l)
del l
print(l)
