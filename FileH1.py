"""
Assignment -4
Task 1- Read a File and handle errors
A Python program that
1. Opens and reads a text file named sample.txt
2. prints its contents line by line
3. Handles errors gracefully if the file does not exists

"""
fh = open("sample.txt","wt")
fh.write("This is a sample text file\n")
fh.write("It contains multiple lines\n")
fh.close()

try:
    with open("sample.txt", "rt") as fh:
         line1 = fh.readline()
         line2 = fh.readline()

    print(f"Line1: {line1}")
    print(f"Line2: {line2}")
except FileNotFoundError as file_err :
    print("The File sample.txt was not found")
    print(file_err)
