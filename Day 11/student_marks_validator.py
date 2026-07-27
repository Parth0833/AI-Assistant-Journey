def student_marks_validator():
    marks = []

    print("=== Student Marks Validator ===")

    # Loop until 5 valid marks are collected
    while len(marks) < 5:
        try:
            # Prompt user for mark
            user_input = input(f"Enter mark {len(marks) + 1} of 5: ")
            mark = int(user_input)

            # Check range rule (0 to 100)
            if 0 <= mark <= 100:
                marks.append(mark)
            else:
                print("Error: Mark must be between 0 and 100. Please try again.")

        except ValueError:
            # Catches non-integer inputs (text, decimals, symbols)
            print("Error: Invalid input! Mark must be an integer. Please try again.")

    # Calculate statistics
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    # Display results
    print("\n--- Summary ---")
    print(f"Marks entered: {marks}")
    print(f"Highest Mark:  {highest}")
    print(f"Lowest Mark:   {lowest}")
    print(f"Average Mark:  {average:.2f}")


# Run the program
student_marks_validator()