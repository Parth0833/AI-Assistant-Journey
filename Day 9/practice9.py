fruits = {'banana','apple','mango','orange','watermelon'}
for fruit in fruits:
    print(fruit)

fruits.add('kiwi')
fruits.add('pineapple')
print(fruits)

fruits.remove('kiwi')
fruits.discard('pineapple')
print(fruits)

numbers = {1,1,1,1,2,2,2,2,2,3,3,3,3,5,5,5,4,4,4,10,10}
unique_num = set(numbers)
print(unique_num)

set1 = {1,2,3}
set2 = {2,3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))


numbers = {1,1,1,1,2,2,2,2,2,3,3,3,3,5,5,5,4,4,4,10,10}
print(4 in numbers)


numbers = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 4, 4, 4, 10, 10]
unique_num = set(numbers)
print(unique_num) 
print(len(unique_num))  