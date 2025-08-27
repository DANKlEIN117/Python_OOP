class Vehicle:
    def __init__(self, name):
        self.name = name  

  

class Car(Vehicle):
    def move(self):
        print(f"The {self.name} is driving")


class Plane(Vehicle):
    def move(self):
        print(f"The {self.name} is flying")


car = Car("Toyota")
plane = Plane("Boeing 747")


car.move()    
plane.move()  
