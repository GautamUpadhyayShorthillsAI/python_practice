from exercie import Shape,Rectangle,Square,Circle,overloadingAdd

def test_rectangle():
    rect = Rectangle(5,2)
    assert rect.area() == 10

def test_square():
    square = Square(5)
    assert square.area() == 25

def test_circle():
    circle = Circle(5)
    assert circle.area() == 3.14*(5**2)
def test_overloading_add_same_type():
    c1 = Circle(3)
    c2 = Circle(3)
    result = overloadingAdd(c1, c2)
    assert result == 2 * (3.14 * 3**2)

def test_overloading_add_different_type():
    c1 = Circle(3)
    rect = Rectangle(10, 5)
    result = overloadingAdd(c1, rect)
    assert result == "Can't add different shape" 

def test_circle_addition():
    c1 = Circle(3)
    c2 = Circle(4)
    # Area of c1 and c2 combined, we check if the radius of new circle is correct
    combined_area = c1.area() + c2.area()
    new_circle = c1 + c2  # This uses the __add__ method
    assert new_circle.area() == combined_area