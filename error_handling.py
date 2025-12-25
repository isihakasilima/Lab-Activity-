def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write("This is a sample text file.\n")
        file.write("It contains multiple lines of text.\n")
        file.write("This is useful for testing file reading.\n")
    print(f"File '{file_path}' created successfully.")

def read_file(file_path):
    file = None
    try:
        file = open(file_path, 'r') 
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: An IOError occurred.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if file is not None:
            file.close()
            print("File has been closed.")

file_path = 'sample.txt'

create_file(file_path)

read_file(file_path)
