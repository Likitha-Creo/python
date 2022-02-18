"""Geometric figures, such as a circle, are other candidates for classes in a program. A circle is uniquely defined by its center point (x0,y0) and its radius R. We can collect these three numbers as data attributes in a class. The values of x0, y0, and R are naturally initialized in the constructor. Other methods can be area and circumference for calculating the area πR2 and the circumference 2πR:"""


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def area(self):
        print(3.14 * self.r * self.r)
    def perimeter(self):
        print(2 * 3.14 * self.r)

c = Circle(10, 20, 5)
c.area()
c.perimeter()


