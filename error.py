filename = input("Please enter the filename: ").strip()

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(f"Content of the file: \n{content}")
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")
except PermissionError:
    print(f"Error: You don't have permission to read the file {filename}.")
except IOError:
    print(f"Error: There was an issue reading the file {filename}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
