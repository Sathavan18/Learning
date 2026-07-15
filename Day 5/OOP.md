A class is a blueprint
An object is an instance created from that blueprint
E.g.:
class Car():
    pass
car1 = Car()
car2 = Car()
car1.brand = 'Toyota'
car1.model = 'Yaris'
car1.year = 2026
car2.brand = 'Ferrari'
car2.model = 'Drive'
car2.year = 2026
print(car1.brand)
print(car1.model)
print(car2.brand)
print(car2.model)

We can use a constructor to give an object its attributes when it's created.
E.g.
class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
car1 = Car('Toyota','Yaris',2026)
car2 = Car('Ferrari','Drive',2026)
print(car1.brand)
print(car2.brand)

Methods define what an object can do.
class Car():
    def __init__(self,brand,model,year,current_year):
        self.brand = brand
        self.model = model
        self.year = year
    def describe(self):
        return f"{self.brand} {self.model} was made in {self.year}"
    def age(self,current_year):
        return current_year - self.year
car1 = Car('Toyota','Yaris',2026)
car2 = Car('Ferrari','Drive',2026)
print(car1.describe())
print(car2.age(2030))