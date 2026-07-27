def safe_file_reader():
    # Prompt user for the filename
    filename = input("Enter filename: ").strip()

    try:
        # Attempt to open and read the file
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("\n--- File Contents ---")
            print(content)

    except FileNotFoundError:
        # Display exact error message if file does not exist
        print("File not found.")


# Run the function
safe_file_reader()