# Create a class named Rectangle, which will have attributes width and height.
# The class should have methods for calculating the perimeter (calculate_perimeter()) and area (calculate_area())
# of the rectangle. Create an instance of the Rectangle class with specific width and height values, and print
# the perimeter and area of the rectangle.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


a = Rectangle(20, 10)
print(a.calculate_area())
print(a.calculate_perimeter())
