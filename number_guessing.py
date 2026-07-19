secret=7
while True:
    num=int(input("Enter a number from 1 to 10 to guess:"))

    if secret==num:
        print("Your guess is correct")
        break
    else:
        print("Oops! pls try again.")