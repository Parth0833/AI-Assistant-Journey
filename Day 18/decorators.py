#A decorator is a function that adds or modifies behavior of another function without changing the original function's code.
def greet():
    print("Hello!")

#We could modify greet function by decorators

#Creating a decorator function
def decorator(function):
    def wrapper():
        print("Starting function....")
        function()
        print("Ending function....")
    return wrapper

greet = decorator(greet)
greet()


#The Syntax for decorators is the @ symbol followed by the decorator function name placed above the function definition.
@decorator
def greet2():
    print("Hello!!")

greet2()

#Decorator with arguments
def greet3(name):
    print("Hello",name)

def decorator_args(funcrion):
    def wrapper(*args, **kwargs):
        print("Before Function")
        function(*args, **kwargs)
        print("After Function")
    return wrapper
greet3("Parth")


def test(*args):
    print(args)

test(20,30,40,50)

def test2(**kwargs):
    print(kwargs)

test2(name="Parth", age=20, city="Kalyan")


#Decorators that return values
def add(a,b):
    return a+b
def decorator(function):
    def wrapper(*args,**kwargs):
        print("Calling Function")
        result = function(*args,**kwargs)
        print("Function Completed")
        return result
    return wrapper

@decorator
def add(a,b):
    return a+b
result = add(20,20)
print(result)

#Functools.wraps
from functools import wraps

def decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    return wrapper