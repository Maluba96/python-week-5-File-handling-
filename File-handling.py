# Task 1: File Creation
def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is line 1: Hello, World!\n")
            file.write("This is line 2: Python programming is fun!\n")
            file.write("This is line 3: Number example - 12345\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"Error occurred while creating/writing the file: {e}")

# Task 2: File Reading and Display
def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    except PermissionError:
        print("Error: You don't have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Task 3: File Appending
def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This is line 4: Adding more content.\n")
            file.write("This is line 5: Learning file handling.\n")
            file.write("This is line 6: 98765 is another number.\n")
        print("Content appended successfully.")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")

# Task 4: Error Handling with try, except, and finally
def manage_file_operations():
    try:
        # Create and write to the file
        create_file()

        # Read and display the file content
        read_file()

        # Append to the file
        append_to_file()

        # Read the file again after appending
        read_file()

    except Exception as e:
        print(f"An error occurred during file operations: {e}")
    finally:
        print("File operations completed.")

# Run the file management script
if __name__ == "__main__":
    manage_file_operations()
