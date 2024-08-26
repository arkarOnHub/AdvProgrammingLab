class OverSpeedError(Exception):
    def __init__(self, message="Speed limit exceeded!"):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, make, model, year, fuel_level, speed):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        self.speed = speed

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

    def accelerate(self, increase):
        self.speed += increase
        if self.speed > 120:
            raise OverSpeedError(f"Speed limit exceeded! Current speed: {self.speed}")
        print(f"Accelerated by {increase} mph. Current speed: {self.speed}")


my_car = Car("Toyota", "Corolla", 2022, 10, 40)

try:
    my_car.accelerate(50)
    my_car.accelerate(60)
    my_car.accelerate(20)
except OverSpeedError as e:
    print(e)
