#Check whether a number is positive or negative
num=int(input("Enter a integer:"))
if num>0:
    print("The number is Positive.")
else:
    print("The number is Negative.")

# Check whether a number is even or odd
num1=int(input("Enter a number:"))
if num1%2==0:
    print("Your number is even.")
else:
    print("Your number is odd.")


#Find the largest of 3 numbers
a=int(input("Enter ur first number:"))
b=int(input("Enter ur second number:"))
c=int(input("Enter ur third number:"))
if a>b and a>c:
    print("The Largest number is ",a)
elif b>c:
    print("The Largest number is ",b)
else:
    print("The Largest number is",c)

#Check whether a person can vote or not
age=int(input("Enter your age:"))
citizen=input("Are you a citizen of the country? (yes/no):")
if age>=18 and citizen=="yes":
    print("Your eligible to Vote.")
elif age<18 and citizen=="yes":
    print("You are a citizen but not eligible to vote due to age.")
else:
    print("You are not a citizen of the country.")

#Check whether a year is a leap year or not
year=int(input("Enter a year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")

#Take Marks and print the grade of a student
marks=int(input("Enter your marks:"))
if marks>=90:
    print("Your Grade is A")
elif marks>=80:
    print("Your Grade is B")
elif marks>=70:
    print("Your Grade is C")
elif marks>=60:
    print("Your Grade is D")
else:
    print("You are Failed.")
