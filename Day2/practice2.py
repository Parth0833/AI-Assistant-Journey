#Find the remainder when two numbers are divided.
a=10
b=2
print("Remainder if a is divided by b:",a%b)

#Find the square and cube of a number.
a=int(input("Enter a number to find square and cube:"))
print("Square of",a,"is:",a**2)
print("Cube of",a,"is:",a**3)

#Check if one number is greater than another.
c=int(input("Enter first number:"))
d=int(input("Enter second number:"))
if c>d:
    print("C is greater than D")
else:
    print("D is greater than C")

#Take age as input and print whether the person is eligible to vote (age >= 18). (Just print True or False for now.)
age=int(input("Enter your age:"))
if age>=18:
    print("Your Applicable for Voting:",True)
else:
    print("Your Not Applicable for Voting:",False)

#Use assignment operators (+=, -=, *=, /=) on a variable and print the result after each operation.
x=20
x+=5
print("After Addition:",x)
x-=3
print("After Subtraction:",x)
x*=2
print("After Multiplication:",x)
x/=4
print("After Division:",x)


#Challenge Shopping bill
print("="*20)
name1=input("Name of the item:")
price1=int(input("Enter the price of the item:"))
quantity1=int(input("Enter the quantity of the item:"))
total=price1*quantity1
print("Your Total Bill is:",total)
print("="*20)
