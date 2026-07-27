#try and except
try:
    num = int(input("Enter a number: "))
    print(100 / num)

except:
    print("Something went wrong!")

print("Program Finished")

#valueerror
try:
    age = int(input("Enter your age: "))
    print(age)

except ValueError:
    print("Please enter numbers only.")

#file not found
try:
    file = open("parth.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found.")

#multiple Exceptions
try:
    num = int(input("Enter Number:"))
    print(100/num)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by Zero.")


#Exception as e
try:
    number = int(input("Enter number:"))
    print(10/number)

except Exception as e:
    print("Error:",e)

#else
try:
    number = int(input("Enter Number:"))
except ValueError:
    print("Invalid input.")
else:
    print("You Entered",number)

#finally
try:
    print("Opening file")

except:
    print("Error")

finally:
    print("Closing file")

#complete Structure
try:
    number = int(input("Enter Number:"))
    
except ValueError:
    print("Value Error")

except ZeroDivisionError:
    print("Division by zero")

else:
    print("Everything worked!")

finally:
    print("Program Finished")