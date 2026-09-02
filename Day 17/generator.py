#A generator is a special type of function that produces values one at a time instead of creating all values at once.

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
for number in numbers():
    print(number)


def count_up_to(n):
    number = 1
    while number <= n:
        yield number
        number +=1
for number in count_up_to(10):
    print(number)

numbers = list(range(1,100))
print(numbers)

def numbers():
    for i in range(1,1000):
        yield i
print(list(numbers()))

#Generator with next()
def numbers():
    yield 10
    yield 20
    yield 30
gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))