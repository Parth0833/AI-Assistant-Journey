#syntax of lambda function lambda argument:expression
#lambda with one argument
square = lambda x: x*x
print(square(10))

cube = lambda x: x**3
print(cube(5))

#Lambda with multiply argument
multiply = lambda a,b:a*b
print(multiply(2,3))

#lambda with conditions
check = lambda x: "Even" if x%2==0 else "Odd"
print(check(5))

