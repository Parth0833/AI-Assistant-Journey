# A mock user state dictionary or object
user = {
    "logged_in": False
}

def requires_login(func):
    def wrapper(*args, **kwargs):
        if user["logged_in"]:
            print("Access granted")#[cite: 13]
            return func(*args, **kwargs)
        else:
            print("Access denied. Please login.")#[cite: 14]
    return wrapper

@requires_login
def profile():
    print("User profile")#[cite: 12]

@requires_login
def settings():
    print("User settings")#[cite: 13]

# Test cases:
print("--- Testing when logged out ---")
profile()

print("\n--- Testing when logged in ---")
user["logged_in"] = True
profile()
settings()# A mock user state dictionary or object
user = {
    "logged_in": False
}

def requires_login(func):
    def wrapper(*args, **kwargs):
        if user["logged_in"]:
            print("Access granted")#[cite: 13]
            return func(*args, **kwargs)
        else:
            print("Access denied. Please login.")#[cite: 14]
    return wrapper

@requires_login
def profile():
    print("User profile")#[cite: 12]

@requires_login
def settings():
    print("User settings")#[cite: 13]

# Test cases:
print("--- Testing when logged out ---")
profile()

print("\n--- Testing when logged in ---")
user["logged_in"] = True
profile()
settings()