import math


# 1. Task: Create a class called `Shape` with a method called `area`. Then, create subclasses `Rectangle` and
# `Circle` that inherit from the `Shape` class. Implement their own `area` method to calculate the area for
# each specific shape.

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# 2. Task: Create a class called `Animal` with a method called `sound` that outputs the sound the animal makes.
# Then, create subclasses `Dog` and `Cat` that inherit from the `Animal` class. Override the `sound` method in
# each subclass to return the specific sound for that animal.

class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return f"Haf"


class Cat(Animal):
    def sound(self):
        return f"Mnouu"


# 3. Task: Create a class called `Employee` with attributes `name` and `salary`. Then, create a subclass called
# `Manager` that inherits from the `Employee` class and has an additional attribute called `department`. Add a method
# called `get_info` that prints information about the employee or manager (name, salary, and optionally department).

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"name: {self.name}\nsalary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get_info(self):
        return f"name: {self.name}\nsalary: {self.salary}\ndepartment: {self.department}"


# 4. Exercise: Create a class called `Vehicle` that has an attribute `speed` and a method `move` which prints
# a message about the vehicle's movement. Then, create subclasses `Car` and `Bike` that inherit from the `Vehicle`
# class and override the `move` method to print a specific message for each type of vehicle.


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move():
        return f"Moving"


class Car(Vehicle):
    def move(self):
        return f"Car is moving"


class Bike(Vehicle):
    def move(self):
        return f"Bike is moving"


# 5. Exercise: Create a class called `Shape` with a method `area`. Then, create a subclass `ThreeDimensionalShape`
# that inherits from the `Shape` class and includes a method `volume`. Implement custom methods for calculating
# the area and volume for different shapes such as `Sphere` or `Cube`.

class Shape:
    def area(self):
        pass


class ThreeDimensionalShape(Shape):
    def volume(self):
        pass


class Cube(ThreeDimensionalShape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return 6 * self.length ** 2

    def volume(self):
        return self.length ** 3


class Sphere(ThreeDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3


# 6. Exercise: Create a class called `Animal` with a method `sound`. Then, create subclasses `Mammal` and `Bird`
# that inherit from the `Animal` class. Each subclass should have its own method `move` that prints the specific
# way of movement for that particular type of animal.


class Animal2:
    def sound(self):
        pass


class Mammal(Animal2):
    def move(self):
        return f"Mammal is walking."


class Bird(Animal2):
    def move(self):
        return f" Bird is Flying."
