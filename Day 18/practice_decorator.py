def log_function(func):
    def wrapper():
        print("function started.")
        func()
        print("Function Finished.")
    return wrapper
@log_function
def hello():
    print("Hello!!")
hello()

#timing decorator
import time
def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Time taken: {end_time - start_time}")
    return wrapper
@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        pass
fast_function()


#Authentication Decorator
class User:
    def __init__(self, name):
        self.name = name
        self.logged_in = False

# Example user instance
user = User("Parth")

def check_login(func):
    def wrapper(*args, **kwargs):
        if user.logged_in == True: #
            return func(*args, **kwargs)
        else:
            print("Please login first.") #
    return wrapper

@check_login
def dashboard():
    print("Welcome to dashboard") #[cite: 6]

# Test cases:
print("--- Test when not logged in ---")
dashboard()

print("\n--- Test when logged in ---")
user.logged_in = True #[cite: 6]
dashboard()