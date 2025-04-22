def modify_file():
    # Get input filename from user
    input_filename = input("Enter the input filename: ")
    
    try:
        # Attempt to open and read the input file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Create output filename by adding '_modified' before the extension
        output_filename = input_filename.rsplit('.', 1)[0] + '_modified.' + input_filename.rsplit('.', 1)[1]
        
        # Modify content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Write modified content to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"File successfully modified and saved as {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    modify_file()