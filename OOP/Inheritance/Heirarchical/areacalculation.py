class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius

class triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    

Rectangle1 = Rectangle(10, 20)
print(f"Area of the rectangle: {Rectangle1.area()}")     

circle1 = circle (5)
print(f"Area of the circle: {circle1.area()}")    

Triangle1 = triangle(10, 20)
print(f"Area of the triangle: {Triangle1.area()}")

 
