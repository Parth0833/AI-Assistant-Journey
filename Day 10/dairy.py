from datetime import date


def add_diary_entry():
    # Ask user for today's entry
    entry = input("Write today's diary:\n")

    # Get current date (YYYY-MM-DD format)
    today = date.today()

    # Open file in append mode ('a') so existing entries aren't overwritten
    with open("diary.txt", "a") as file:
        file.write(f"--- Date: {today} ---\n")
        file.write(f"{entry}\n\n")

    print("\nYour entry has been saved to diary.txt!")


# Run the application
if __name__ == "__main__":
    add_diary_entry()