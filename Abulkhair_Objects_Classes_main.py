import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = math.pi * (self.radius ** 2)
        print(f"Area of the circle with radius {self.radius}: {circle_area:.2f}")

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle with radius {self.radius}: {circle_perimeter:.2f}")

# Example usage:
radius_value = float(input("Enter the radius of the circle: "))
circle_instance = Circle(radius_value)

circle_instance.area()
circle_instance.perimeter()