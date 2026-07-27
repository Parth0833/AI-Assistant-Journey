file = open("notes.txt", "r")
print(file.read())
file.close()

file = open("notes.txt","w")
file.write("Hello Parth")
file.close()

# r for read, w for write, a for append, x for create new file

file = open("notes.txt","r")
content = file.read()
print(content)
file.close()

#appending a data
file = open("notes.txt", "a")
file.write("\nAI")
file.close()

#with open
with open("notes.txt", "r") as file:
    print(file.read())

#Reading line by line
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

#creating a new file
with open("student.txt", "w") as file:
    file.write("Parth")

with open("notes.txt", "r") as file:
    lines = file.readlines()

print(lines)

