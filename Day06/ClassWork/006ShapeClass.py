import math
class Shape:
    def calculate_area(self):
        print("Area calculation not found")
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length * self.width 
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return math.pi*(self.radius)**2
rect=Rectangle(10,5)
circle=Circle(7)
print(f"The ractangle area: {rect.calculate_area()}")
print(f"The circle area: {circle.calculate_area()}")