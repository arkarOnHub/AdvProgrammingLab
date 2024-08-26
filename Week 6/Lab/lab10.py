import time
import threading


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
        self.running = False

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

    def drive(self):
        self.running = True
        while self.running and self.fuel_level > 0:
            print(f"Driving... Speed: {self.speed} km/h")
            self.fuel_level -= 1
            time.sleep(2)
        if self.fuel_level <= 0:
            print("Fuel level is too low! Stopping the car.")
            self.running = False

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

    def diagnostics(self):
        while self.running:
            print(f"Car diagnostics:")
            print(f"  Make: {self.make}")
            print(f"  Model: {self.model}")
            print(f"  Year: {self.year}")
            print(f"  Fuel Level: {self.fuel_level}")
            print(f"  Speed: {self.speed}")
            print(f"  Color: {self.color}")
            time.sleep(1)


my_car = Car("Toyota", "Corolla", 2022, 10, 60)

my_car.read_color_from_file("color.txt")

diagnostics_thread = threading.Thread(target=my_car.diagnostics)
diagnostics_thread.start()

driving_thread = threading.Thread(target=my_car.drive)
driving_thread.start()

diagnostics_thread.join()
driving_thread.join()
