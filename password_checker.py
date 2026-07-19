correct_pass="python123"

while True:
    password=input("Enter your password:")
    
    if password== correct_pass:
        print("Access Granted")
        break
    else:
        print("Access denied, Pls Try again.")