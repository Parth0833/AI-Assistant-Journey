#Login User
correct_username="admin"
correct_password="admin123"
username=input("Enter your username:")
password=input("Enter your password:")
if username==correct_username and password==correct_password:
    print("Login Succesful. Welcome", username)
else:
    print("Login Failed. Please enter correct username and password.")