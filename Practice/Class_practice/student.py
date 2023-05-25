# Create a class named Student, which will have attributes name, age, and grades. The class should have a method
# for adding a grade (add_grade()), which will take a numerical value and add it to the grades list.
# Create an instance of the Student class with a specific name and age, and then add several grades using
# the add_grade() method. Finally, print the student's name, age, and the list of their grades.

class Student:
    def __init__(self, name, age):
        self.grade = None
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGrades: {self.grades}\n"


a = Student("Richard", 28)
b = Student("Roman", 22)
c = Student("Lucie", 21)
a.add_grade(1)
a.add_grade(2)
b.add_grade(5)
b.add_grade(1)

print(a)
print(b)
print(c)
