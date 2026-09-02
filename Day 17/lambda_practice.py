#Create Lambda that calculates squares
num = int(input("Enter the number to be squared:"))
square = (lambda x: x*x)(num)
print("The square of given number",num,"is",square)

#Create a lambda that checks whether a number is positive or negative.
number = int(input("Enter the number to check wether it is positive or negative:"))
pos_neg = lambda x:"Positive" if number > 0 else( "Negative" if number < 0 else "Zero")
print("The given number",number,"is",pos_neg(number))

#use map to double
numbers = [1, 2, 3, 4, 5]
double = map(lambda x: x*2,numbers)
print("Double of the given list is:",list(double))

#Use filter to extract number grater than 10
given = [5, 12, 8, 20, 3, 15]
result = filter(lambda x: x>10,given)
print("Numbers grater than 10 are:",list(result))

#sort students according to marks using lambda
students = [
    ("Parth",90),
    ("Amay",70),
    ("Shinde",89)
]
students.sort(key=lambda student:student[1], reverse=True)
print("Highest marks students are:",students)

