def even_numbers(n):
    for i in range(2, n+1,2):
        yield i
for number in even_numbers(100000):
    print(number)
