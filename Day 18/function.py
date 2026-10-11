#Functions are objects
def greet():
    print("Hello!")

say_hello = greet
say_hello()

#Passing a function to another function also the foundation of decorators
def greet2():
    print("Hello!!")

def execute_function(function):
    function()

execute_function(greet2)

#Returning a function 
def outer():
    def inner():
        print("Hello from inner function!!.")

    return inner
result = outer()
result()