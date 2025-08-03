def file_read_write_challenge():
    with open('input.txt', "r") as input_txt:
        contents=input_txt.read()

        modified_contents=contents.upper()

        with open('output.txt','w') as output_txt:
            output_txt.write(modified_contents)
        print("File has been read, modified, and saved as output.txt")



if __name__=="__main__":
    file_read_write_challenge()