"""
Assignment -4
Task 2 :- Write and append data to a file
A Python program that
    1. Takes user input and writes it to a file named output.txt
    2. Appends additional data to the same file
    3. Reads and displays the final content of the file
"""

text=str(input("Enter the text to write into the file : "))
with open ("output.txt","w") as fh:
    fh.write(text + "\n")
print("Data successfully written to output.txt")

app=str(input("Enter additional text to append:"))
with open("output.txt","a") as fh:
    fh.write(app)
print("Data successfully appended to output.txt")

print("Final content of output.txt\n")
with open("output.txt","r") as fh:
    print(fh.read())

