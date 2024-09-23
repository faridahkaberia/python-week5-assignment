# File creation, writing, and appending functionality

# Define the file name
file_name = "my_file.txt"

# Function to write to the file
def create_and_write_file():
    try:
        # Open the file in write mode ('w') 
        with open(file_name, 'w') as file:
            # Write three lines of text (including numbers)
            file.write("My name is Faridah.\n")
            file.write("I am 28 years old.\n")
            file.write("I love coding.\n")
        print(f"File '{file_name}' created and written to successfully.")
    except Exception as e:
        print(f"Error creating or writing to the file: {e}")

# Function to read and display the contents of the file
def read_file():
    try:
        # Open the file in read mode ('r')
        with open(file_name, 'r') as file:
            # Read the contents of the file
            content = file.read()
            print("\n--- File Contents ---")
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error reading the file: {e}")

# Function to append to the file
def append_to_file():
    try:
        # Open the file in append mode ('a')
        with open(file_name, 'a') as file:
            # Append three additional lines of text
            file.write("My new hobby is art.\n")
            file.write("It took me 10 weeks to learn.\n")
            file.write("It is therapeutic.\n")
        print(f"Appended to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error appending to the file: {e}")

# Main script
try:
    # Create and write to the file
    create_and_write_file()

    # Read and display the file contents
    read_file()

    # Append to the file
    append_to_file()

    # Read and display the file contents after appending
    read_file()

finally:
    print("\nFile handling operations completed.")
