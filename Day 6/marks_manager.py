marks = []

for i in range(1, 6):
    mark = int(input("Enter marks obtained by student in python: "))
    marks.append(mark)  
print("Maximum marks:", max(marks))
print("Minimum marks:", min(marks))

avg = sum(marks) / len(marks)
print("Average of all students is:", avg)