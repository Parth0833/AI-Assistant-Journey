class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        else:
            self.speed = self.speed

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Speed:", self.speed)

car1 = Car("Toyota", "Camry", 60)
car1.display_info()
print("="*10)
car1.accelerate()
car1.display_info()
print("="*10)
car1.brake()
car1.display_info()
print("="*10)
car1.brake()
car1.brake()
car1.brake()
car1.brake()
car1.brake()
car1.display_info()
car1.brake()
car1.display_info()
car1.brake()
car1.display_info()