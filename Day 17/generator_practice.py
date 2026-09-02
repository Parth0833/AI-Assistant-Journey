def numbers(n):
    number = 1
    while number <= n:
        yield number
        number +=1
for number in numbers(5):
    print(number)

#even numbers from 2 to 20
def even_numbers():
    for i in range(2,21,2):
        yield i
for numbers in even_numbers():
     print(numbers)

#Generator that produces square of a number
def square_numbers(n):
    for i in range(1,n+1):
        yield i*i
for number in square_numbers(5):
     print(number)

#Generator that counts backwards
def count_backwards(n):
    while n > 0:
        yield n
        n-=1
for number in count_backwards(5):
     print(number)

     