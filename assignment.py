def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode and write the modified content
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Content successfully written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print("Error: Could not read or write the file.")

# Example usage
read_and_modify_file('C:/Users/admin/Documents/plp2025/python/week4/example.txt', 'output.txt')
