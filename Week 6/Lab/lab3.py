class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        try:
            if self.make == "Unknown":
                raise ValueError("Cannot start the engine of an unknown make.")
            print("Engine started.")
        except ValueError as e:
            print(f"Error: {e}")


car1 = Car("Toyota", "Corolla")
car1.start_engine()

car2 = Car("Unknown", "ModelX")
car2.start_engine()
