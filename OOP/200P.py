class Vehicle:
    def __init__(self, mileage, average):
        self.mileage = mileage
        self.average = average

modelY = Vehicle(30, 40)
print("ModelY's Mileage is", modelY.mileage, "and Average is", modelY.average)
