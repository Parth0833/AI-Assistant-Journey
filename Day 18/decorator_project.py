def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        print(f"Arguments: {args}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

@logger
def multiply(a, b):
    return a * b

@logger
def greet(name):
    return "Hello " + name

# Testing the functions:
add(10, 20)
print()
multiply(4, 5)
print()
greet("Parth")