#An iterator is an object that allows you to access elements one at a time.

numbers = [10,20,30,40]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#Examples of iterables:
#List
#Tuple
#String
#Dictionary
#Set

#NEXT() 
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))