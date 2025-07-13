class vehicle:
    def __init__ (self, name, mileage, max_speed):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed

class Bus(vehicle):
    pass
School_bus = Bus("School Volvo", 12, 180)
print("Vehicle Name:", School_bus.name)
print("Mileage:", School_bus.mileage, "kmpl")
print("Max Speed:", School_bus.max_speed, "km/h")
print("Vehicle Type: Bus")