import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

def generate_password(length):
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

length = int(input("Enter password length: "))

print("Generated Password:", generate_password(length))