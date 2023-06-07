# 1. Example: Create the classes `Employee` and `Person`. Then create the class `Manager` that inherits
# from both `Employee` and `Person`. The `Employee` class contains the `salary` attribute and the `get_salary`
# method, which returns the salary value. The `Person` class contains the `name` and `age` attributes, and the
# `get_info` method, which returns information about the person. The `Manager` class should inherit properties
# from both classes and include the `get_info` method, which prints information about the manager (name, age, salary).

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Manager(Employee, Person):
    def __init__(self, name, age, salary):
        Employee.__init__(self, salary)
        Person.__init__(self, name, age)

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


# 2. Example: Create the classes `Shape` and `Color`. Then create the class `ColoredShape` that inherits from both
# `Shape` and `Color`. The `Shape` class contains the `area` method, and the `Color` class contains the `color`
# attribute. The `ColoredShape` class should inherit properties from both classes and include the `display_info`
# method, which prints information about the shape and its color.

class Shape:
    def __init__(self, shape):
        self.shape = shape

    def area(self):
        return self.shape


class Color:
    def __init__(self, color):
        self.color = color

    def object_color(self):
        return self.color


class ColoredShape(Shape, Color):
    def __init__(self, color, shape):
        Color.__init__(self, color)
        Shape.__init__(self, shape)

    def display_info(self):
        shape = Shape.area(self)
        color = Color.object_color(self)
        return f"{shape}, {color}"


# 3. Example: Create the classes `Vehicle` and `Engine`. The `Vehicle` class contains the `move` method, and the
# `Engine` class contains the `start` method. Then create the class `Car` that inherits from both `Vehicle` and
# `Engine`. The `Car` class should inherit properties from both classes and have an additional `drive` method,
# which prints a message about driving the car.

class Vehicle:

    def move_method(self):
        return "car is moving"


class Engine:

    def start_method(self):
        return "car is starting"


class Car(Vehicle, Engine):

    def drive_method(self):
        move = Vehicle.move_method(self)
        start = Engine.start_method(self)
        return f"{start} - {move}"
