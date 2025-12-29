def create_file(file_path):
    with open(file_path, "w") as file:
        file.write("This is a sample text file.\n")
        file.write("Overview\n")
        file.write("This script demonstrates basic file handling. It shows how to:\n")
        file.write("Create file and write content to it.\n")
        file.write("Read the content of the file.\n")
        file.write("Ensure that file is properly closed using a finally block.\n")

    print(f"File '{file_path}' created successfully.")


def read_file(file_path):
    file = None
    try:
        file = open(file_path, "r")
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


file_path = "sample.txt"

create_file(file_path)
read_file(file_path)
