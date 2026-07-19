# 1. Define the math operations first with return statements
def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    if b == 0:
        return "Error: Division by zero"
    return a / b

# 2. Define the main calculator function
def sci_cal(operation, a, b): 
    if operation == "add": 
        print(add(a, b))
    elif operation == "subtract": 
        print(subtract(a, b))
    elif operation == "multiply": 
        print(multiply(a, b))
    elif operation == "divide": 
        print(divide(a, b))
    else: 
        print("Invalid input.")

# 3. Call the function with string names and separate number arguments
sci_cal("add", 10, 10)
