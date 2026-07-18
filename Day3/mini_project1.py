#ATM pin checker
correct_pin=2424
pin=int(input("Enter your 4 digit pin:"))
if pin==correct_pin:
    print("Your pin is correct. You can Access your account.")
else:
    print("Your pin is incorrect. Please try again.")