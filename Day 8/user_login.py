# Store users (username -> password)
users = {
    "admin": "1234",
    "parth": "python",
    "guest": "guest123"
}

# Ask for inputs
username = input("Username: ")
password = input("Password: ")

# Check credentials
if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Login Failed")