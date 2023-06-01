# Create a class called Car that represents an automobile. The class should have attributes such as make (manufacturer),
# model, year (manufacturing year), and mileage (total miles driven). Add a method called drive() that takes the number
# of miles driven as input and adds it to the mileage attribute. Create an instance of the Car class with specific
# values and test the drive() method.


class Car:
    def __init__(self, manufacturer, model, year, total_mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.total_mileage = total_mileage

    def drive(self, miles):
        self.total_mileage += miles

    def __str__(self):
        return (
            f"Manufacturer: {self.manufacturer}\nModel: {self.model}\nProduction year: "
            f"{self.year}\nMileage: {self.total_mileage}\n"
        )


a = Car("Volvo", "C60", 2019, 25000)
a.drive(520)
print(a)
a.drive(5624)
print(a)
