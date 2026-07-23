#creating sets
fruits = {'Banana','Apple','Mango'}
print(fruits)

#Duplicate values
number = {1,1,1,2,2,3,3,3,3,4,5,5,5}
print(number)

#adding element
fruits = {'Banana','Apple','Mango'}
fruits.add('Orange')
print(fruits)

#removing elements
fruits.discard('Banana')
print(fruits)

#loop through a set
fruits = {'Banana','Apple','Mango'}
for fruit in fruits:
    print(fruit)

#length of set
print(len(fruits))

#Membership test
fruits = {'Banana','Apple','Mango'}
print('Apple' in fruits)
print('Kiwi' in fruits)

#union
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.union(set2))

#Intersection
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.intersection(set2))

#Difference
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.difference(set2))

#clear a set
set1 = {1,2,3}
set2 = {4,5,6}
set1.clear()
print(set1)
