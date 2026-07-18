#number gussing game
secret_number=7
guess=int(input("Guess the secret number between 1 and 10:"))
if guess==secret_number:
    print("Congratulations! You guessed the correct number.")
else:
    print("Sorry, that's not the correct number. The secret number was", secret_number)
    