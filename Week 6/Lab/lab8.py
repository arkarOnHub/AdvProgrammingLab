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
        self.color = None

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

    def read_color_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read().strip()
                if not content:
                    raise ValueError("The file is empty.")
                self.color = content
            print(f"Car color read from file: {self.color}")
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


my_car = Car("Toyota", "Corolla", 2022, 10, 40)

print("Testing with the correct file path:")
my_car.read_color_from_file("color.txt")

print("\nTesting with an incorrect file path:")
my_car.read_color_from_file("nonexistent_file.txt")

print("\nTesting with an empty file:")
with open("empty_color.txt", "w") as empty_file:
    pass
my_car.read_color_from_file("empty_color.txt")