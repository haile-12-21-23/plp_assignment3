def file_read_write_challenge():
    try:
        with open('input.txt', "r") as input_txt:
          contents=input_txt.read()

        modified_contents=contents.upper()

        with open('output.txt','w') as output_txt:
            output_txt.write(modified_contents)
        print("File has been read, modified, and saved as output.txt")
    except FileNotFoundError:
        print("File not found.")

def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")

    try:
          with open(filename,'r') as file:
              contents=file.read()
              print("\nFile contents:\n")
              print(contents)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
     print(f"An unexpected error occurred: {e}")




if __name__=="__main__":
    file_read_write_challenge()
    read_file_with_error_handling()