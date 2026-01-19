
class Vehicle:

    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle is starting")



class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def drive(self):
        print("Car is being driven")



class ElectricCar(Car):
    def __init__(self):
        super().__init__()

    def charge(self):
        print("Electric car is charging")


v1 = Vehicle()
c1 = Car()
e1 = ElectricCar()

# Method calls
v1.start()
c1.start()
c1.drive()
e1.start()
e1.drive()
e1.charge()

# Display class variable
print("Total vehicles created:", Vehicle.vehicle_count)
