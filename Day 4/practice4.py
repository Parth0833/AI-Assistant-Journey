#print numbers from 1 to 10
for i in range(1,11):
    print(i)

#print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

#print even numbers from 1 to 100
for i in range(2, 101,2):
    print(i)

#print odd numbers from 1 to 100
for i in range(1,101,2):
    print(i)

#print multiplication number of any table
for i in range(1,11):
    print("5 x",i,"=",5*i)

#find the sum of number 1 to 100
total = 0
count = 1
while count <= 100:
    total += count
    count += 1
print(total)

#to find the factorial of a number
num = 5
factorial = 1
i = num

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # Multiply and decrement until i reaches 1
    while i > 0:
        factorial *= i
        i -= 1

    print(f"The factorial of {num} is {factorial}")