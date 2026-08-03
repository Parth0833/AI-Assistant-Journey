class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Speed: {self.speed}")

car1 = Car("BMW", "M5", 300)
car2 = Car("BMW", "M2", 250)

car1.display_info()
print()
car2.display_info()
car1.accelerate()
print()
print("After accelerating car1:")
car1.display_info()