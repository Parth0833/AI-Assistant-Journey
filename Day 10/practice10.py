#practice oquestion 1
file = open("hello.txt","w")
file.write("Hello Python!")
file.close()

file = open("hello.txt","r")
content = file.read()
print(content)

file = open("hello.txt","w") 
file.write("welcome to ai engineering")
file.close()
file = open("hello.txt","r")
content = file.read()
print(content)

#question 2
# 1. Create a file containing five names
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# 2. Read the file line by line
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())


#count lines
# Open the file in read mode and count each line
line_count = 0

with open("names.txt", "r") as file:
    for line in file:
        line_count += 1

print(f"Total lines: {line_count}")

#question 3
word_count = 0

# Open the file in read mode
with open("names.txt", "r") as file:
    for line in file:
        words = line.split()  # Splits the line into a list of words
        word_count += len(words)  # Adds the number of words in this line to the total

print(f"Total words: {word_count}")

#question 4
# Open the source file in read mode and destination file in write mode
with open("hello.txt", "r") as source_file, open("names.txt", "w") as target_file:
    for line in source_file:
        target_file.write(line)