# Koenigsegg class (Jesko Absolut)
class Koenigsegg:
    def engine(self):
        print("Engine: Twin-turbocharged 5.0L V8")

    def power(self):
        print("Power Output: Over 1,600 hp with E85 fuel")

    def transmission(self):
        print("Transmission: 9-speed Light Speed Transmission (LST), clutch-by-wire")

    def details(self):
        print("Notable For: 500+ km/h top speed, cutting-edge engineering, active aero")
        print("Type: Hypercar")
        print("Country: Swedish")

# Lotus class (Emira & Evija)
class Lotus:
    def engine(self):
        print("Engine: 2.0L turbo inline-4 / 3.5L supercharged V6 (Emira) or Electric (Evija)")

    def power(self):
        print("Power Output: 360–400 hp (Emira) or 2,000 hp (Evija)")

    def transmission(self):
        print("Transmission: 6-speed manual or automatic (Emira)")

    def details(self):
        print("Notable For: Lightweight design, driver-focused handling, minimalist performance")
        print("Type: Sports car (Emira) / Electric hypercar (Evija)")
        print("Country: British")

# Polymorphic function
def show_car_specs(car):
    print(f"\n--- {car.__class__.__name__} Specifications ---")
    car.engine()
    car.power()
    car.transmission()
    car.details()
    print("-" * 50)

# Driver code
cars = [Koenigsegg(), Lotus()]

for car in cars:
    show_car_specs(car)
