class Animals:
    def eat(self):
        print("Eating...")

    def sleep(self):
        print("sleeping...")

class Dog(Animals):
    def bark(self):
        print("Woof! Woof!")

dog= Dog()
dog.eat()
dog.sleep()
dog.bark()
print("="*20)
class Vehicle:
    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    def honk(self):
        print("Hoking...")

car = Car()
car.start()
car.honk()