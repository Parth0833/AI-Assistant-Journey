#creating lists
fruit = ["apple","banana","orange","watermelon"]
print(fruit)

#Indexing
fruit = ["apple","banana","orange","watermelon"]
print(fruit[0])
print(fruit[1])

#negative indexing
print(fruit[-3])

#Modifing a list
fruit[1]="mango"
print(fruit)

#Adding items
fruit.append("Grapes") #adds at the end
print(fruit)

fruit.insert(1,"Kiwi")
print(fruit)#insert in between any where

#removing items
fruit.remove("orange")
print(fruit)
#or
fruit.pop()#removes last element

#List length
print(len(fruit))

#Loops in lists
for fruits in fruit:
    print(fruits)

#Useful functions
numbers=[1,5,10,6,21,4,]

print(max(numbers))
print(min(numbers))
print(sum(numbers))

#Sorting
numbers.sort()
print(numbers)
