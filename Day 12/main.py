import calculator

print(calculator.add(10,20))
print(calculator.sub(10,5))

#different methods to import
from calculator import add,sub
print(add(10,20))
print(sub(10,2))

#Using as: sometimes module names are too long
import calculator as calc
print(calc.add(10,5))

#python builtin modules
import random #random is a module used for random things generation like random number.
print(random.randint(1,10))

import math #all the maths functions are in this module
print(math.sqrt(100))
print(math.factorial(5))
print(math.pi)

import datetime
current_datetime = datetime.datetime.now()
print(current_datetime)

