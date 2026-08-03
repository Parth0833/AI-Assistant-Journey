# Parent Class
class Vehicle:

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"The engine of {self.brand} {self.model} is now running."


# Child Class 1
class Car(Vehicle):

    def open_trunk(self):
        """Unique method for Car"""
        return f"Opening the trunk of the {self.brand} {self.model}."


# Child Class 2
class Bike(Vehicle):

    def wheelie(self):
        """Unique method for Bike"""
        return f"The {self.brand} {self.model} is performing a wheelie! 🏍️"


# Child Class 3
class Truck(Vehicle):

    def load_cargo(self, weight_in_kg: int):
        """Unique method for Truck"""
        return f"Loaded {weight_in_kg}kg of cargo into the {self.brand} {self.model}."


# Example Usage
if __name__ == "__main__":
    my_car = Car("Toyota", "Camry")
    my_bike = Bike("Yamaha", "MT-07")
    my_truck = Truck("Volvo", "FH16")

    # Shared inherited method
    print(my_car.start_engine())

    # Unique methods for each child class
    print(my_car.open_trunk())
    print(my_bike.wheelie())
    print(my_truck.load_cargo(1500))