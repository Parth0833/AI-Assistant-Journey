#Divide two numbers
def safe_divide():
    try:
        # Ask for input and convert to floats
        num1 = float(input("Enter the numerator (first number): "))
        num2 = float(input("Enter the denominator (second number): "))

        # Perform division
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

    except ValueError:
        # Handles non-numeric inputs
        print("Error: Invalid input. Please enter valid numerical values.")

    except ZeroDivisionError:
        # Handles division by zero
        print("Error: Cannot divide by zero.")


# Run the function
safe_divide()

def check_age():
    try:
        # Ask the user for age and convert to an integer
        age = int(input("Please enter your age: "))

        # Optional check for negative age values
        if age < 0:
            print("Error: Age cannot be a negative number.")
        else:
            print(f"Thank you! Your age is recorded as {age}.")

    except ValueError:
        # Handles text or non-integer inputs
        print("Error: Invalid input. Please enter a valid number for age.")


# Run the function
check_age()

filename = "non_existent_file.txt"

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

try:
    # Example operation that triggers an exception
    result = 10 / 0
except Exception as e:
    # Catch any general exception and print its exact message
    print(f"An error occurred: {e}")


try:
    # Code that might cause an error
    num = float(input("Enter a positive number: "))
    result = 100 / num

except ValueError:
    # Runs if input conversion fails
    print("Error: That was not a valid number!")

except ZeroDivisionError:
    # Runs if division by zero occurs
    print("Error: You cannot divide by zero!")

else:
    # Runs ONLY if NO exceptions occurred in the try block
    print(f"Success! 100 divided by {num} is {result}")

finally:
    # ALWAYS runs regardless of whether an exception occurred or not
    print("Execution complete: Cleanup finished.")


def calculator():
    print("=== Simple Robust Calculator ===")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # Get operation choice
    choice = input("Select an operation (1-4): ").strip()

    # Validate menu choice
    if choice not in ["1", "2", "3", "4"]:
        print("Error: Invalid choice. Please select 1, 2, 3, or 4.")
        return

    # Get numerical inputs with exception handling
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input! Please enter valid numbers.")
        return

    # Perform chosen operation
    if choice == "1":
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == "4":
        try:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")


# Run the calculator
calculator()

def read_user_file():
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ").strip()

    try:
        # Safely open and read the file
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
            print("\n--- File Contents ---")
            print(contents)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
read_user_file()


