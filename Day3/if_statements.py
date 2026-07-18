#only if statements
age=21
if age>=18:
    print("Your Eligible to vote.")

#if else statements
age=17
if age>=18:
    print("Your Eligible to vote.")
else:
    print("Your not Eligible to Vote.")

#if elif else statements
marks=int(input("Enter your marks:"))
if marks>=90:
    print("Your Grade is A+")
elif marks>=80:
    print("Your Grade is A")
else:
    print("Your Grade is C")

#Nested if statements
age=20
citizen=True
if age>=18:
    if citizen:
        print("Your Eligible to vote.")
        