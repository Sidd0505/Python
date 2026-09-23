class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
    
    def start(self):
        print(f"{self.make} {self.model} {self.year} starts.")
    
    def stop(self):
        self.speed = 0
        print(f"{self.make} {self.model} {self.year} stops.")
    
    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.make} {self.model} {self.year} accelerates. Current speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def open_doors(self):
        print(f"Opening {self.num_doors} doors of {self.make} {self.model} {self.year}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def wheelie(self):
        print(f"{self.make} {self.model} {self.year} pops a wheelie!")

# Creating instances of Car and Motorcycle
my_car = Car("Toyota", "Camry", 2022, 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2020, 2)

# Using methods of the instances
my_car.start()
my_car.open_doors()
my_car.accelerate(60)
my_car.stop()

my_motorcycle.start()
my_motorcycle.accelerate(80)
my_motorcycle.wheelie()
my_motorcycle.stop()



#########Output##########
Toyota Camry 2022 starts.
Opening 4 doors of Toyota Camry 2022
Toyota Camry 2022 accelerates. Current speed: 60 km/h
Toyota Camry 2022 stops.
Harley-Davidson Sportster 2020 starts.
Harley-Davidson Sportster 2020 accelerates. Current speed: 80 km/h
Harley-Davidson Sportster 2020 pops a wheelie!
Harley-Davidson Sportster 2020 stops.
