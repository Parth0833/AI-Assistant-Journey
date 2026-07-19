#understanding function
def greet():
    print("Welcome to AI Enginnering.")
greet()

# Parameters and arguments
def greet(name):
    print("Hello", name)
greet("Path")
greet("Amay")
greet("Prathmesh")

#multiple parameters
def add(a,b):
    print("Sum is",a+b)
add(1,2)
add(4,10)

#Return Value
def square(num):
    return num*num
result = square(5)
print(result)


#Local vs Global variable
name= "Parth"
def display():
    print(name)
display() #here name is global variable

def display():
    age = 20
    print(age)
display() #now age exists inside the function is now local variable


