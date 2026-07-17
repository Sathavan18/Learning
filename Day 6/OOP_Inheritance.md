Inheritance allows one class to inherit attributes and methods from another class. 
E.g.:
class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def describe(self):
        return f'{self.brand} was made in {self.year}.'

class Car(Vehicle):
    pass

car1 = Car('Toyota', 2026)
print(car1.describe())

Exending a parent class with super()
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year) # calls parent constructor
        self.model = model

Exercise:
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def describe(self):
        return f'{self.name} has a {self.salary} salary'

class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language = programming_language

developer1 = Developer('Sathavan',30000,'Python')

print(developer1.name)
print(developer1.salary)
print(developer1.programming_language)
print(developer1.describe())