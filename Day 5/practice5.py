#create a function that displays ur name
def display():
    print("My name is : Parth")
display()

#Create function that add 2  numbers
def add(a,b):
    print("Addition of this two numbers are:", a+b)
add(1,2)
add(5,100)

#Create a function that multiplies 2 numbers
def mul(a,b):
    print("The multiplication of two numbers are:",a*b)
mul(7,10)
mul(25,25)

#Create a function that returns the square of a number
def square(a):
    return a*a
result=square(10)
print(result)

#Create function that checks whether number is even or odd
def even_odd(num):
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
result1 = even_odd(1102303343)
print(result1)

#Create function that finds largest of 3 numbers
def largest_num(a,b,c):
    if a>b and a>c:
        print("a is the Largest number.")
    elif b>c and b>a:
        print("b is the Largest Number.")
    elif c>a and c>b:
        print("c is the largest number.")
    else:
        print ("all the numbers are equal.")

largest_num(123, 987 ,123)

#Create a function which calculates the factorial of the function
def factorial_num(num):
    factorial=1
    i=num
    while num > 0:
        factorial *= num
        num -= 1
    print(factorial)
factorial_num(5)
