#Create a List of 5 fruits
fruits=["Apple","Mango","Watermelon","Banana","Orange"]
print(fruits)

#Create a list of number and print largest,smallest and sum
number=[ 1, 5, 10, 15, 2, 7, 12]
print(max(number))
print(min(number))
print(sum(number))

#Take 5 marks from user and store them in lists and print them
marks=[]
for i in range(1,6):
    mark=int(input("Enter marks of 5 subjects:"))
    marks.append(mark)
avg= sum(marks)/ len(marks)

print("Your avg marks are:",avg)

#revrse a list
number=[ 1, 5, 10, 15, 2, 7, 12]
number.reverse()
print(number)

#Sort a lst
number=[ 1, 5, 10, 15, 2, 7, 12]
number.sort()
print(number)

#remove duplicate element
number=[ 1, 5, 10, 15, 2, 7, 12, 7, 5, 12, 1]
clean_list=list(set(number))
print(clean_list)

