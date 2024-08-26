class Car:
    def __init__(self, make, model, year, fuel_level):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level

    def start_engine(self):
        try:
            if self.make == "Unknown":
                raise ValueError("Cannot start the engine of an unknown make.")
            print("Engine started.")
        except ValueError as e:
            print(f"Error: {e}")

    def check_fuel(self):
        if self.fuel_level < 5:
            raise ValueError("Fuel level is too low!")

    def drive(self, distance):
        self.fuel_level -= distance
        self.check_fuel()
        print(f"Drove {distance} miles. Fuel level: {self.fuel_level}")


my_car = Car("Toyota", "Corolla", 2022, 10)

try:
    my_car.drive(3)
    my_car.drive(4)
    my_car.drive(3)
except ValueError as e:
    print(e)
