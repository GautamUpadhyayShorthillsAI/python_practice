class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
    def __repr__(self):
        return "Shape"

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def __repr__(self):
        return "Rectangle"
    
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
    
    def __repr__(self):
        return "Square"
    

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def __repr__(self):
        return "Circle"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            # Example: return a new Circle with the combined area (as a radius approximation)
            combined_area = self.area() + other.area()
            return Circle((combined_area / 3.14) ** 0.5)  # Back to radius based on area
        return NotImplemented

def overloadingAdd(a,b):
    if(type(a) != type(b)):
        return "Can't add different shape"
    else:
        return a.area() + b.area()


c1 = Circle(3)  
c2 = Circle(3)  

rect = Rectangle(10, 5)
square = Square(4)
circle = Circle(3)
newC = c1 + c2
print(square.area())
print(newC.area())
print(overloadingAdd(c1,c2))