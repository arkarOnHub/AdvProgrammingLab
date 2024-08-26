class Car:

    def __init__(self, model, year):
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.year} {self.model} car is driving.")
