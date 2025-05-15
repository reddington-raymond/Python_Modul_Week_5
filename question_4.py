'''
Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:

##### Features:
- "make" (Brand of vehicle)
- "model" (Vehicle model)
- "year" (Year of manufacture of the vehicle)

Create a "Vehicle" class and create two derived subclasses, "Off-Road Vehicle" (SUV) and "SportsCar" classes.

- The "Off-Road Vehicle" class inherits from the "Vehicle" class and adds an additional "four_wheel drive" feature.
- Let the "SportCar" class inherit from the "Vehicle" class and add a "max_speed" property.

Create an instance of each class, determine its properties, and write a program to display these properties.
'''

class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
    def __str__(self):
        return f"Bu {self.make} {self.model} arac {self.year} modeldir."
        
class OffRoad(Vehicle):
    def __init__(self, make, model, year, is_four_wheel): #Is_four_wheel degiskeni eger arac 4 cekerse True degerini alir.
        super().__init__(make, model, year)
        self.is_four_wheel=is_four_wheel
    
    def __str__(self):
        if self.is_four_wheel:
            return f"Bu {self.make} {self.model} arac {self.year} modeldir ve dort cekerlidir."
        return super().__str__()
    

class SportsCar(Vehicle):
    def __init__(self, make, model, year, max_speed):
        super().__init__(make, model, year)
        self.max_speed=max_speed
    
    def __str__(self):
        return f"Bu {self.make} {self.model} arac {self.year} modeldir ve maksimum hizi {self.max_speed} km/sa'dir."
    
vehiche1=Vehicle('Toyota', 'Corolla', 2019)
offroad1=OffRoad('Chavrolet', 'Tahoma', 2013, True)
sportscar1=SportsCar('Porsche', 'Carrera', 2025, 294)

print(vehiche1)
print(offroad1)
print(sportscar1)



        
