"""Assignment 5
Task 1 : To create a dictionary of Student marks
A Python program that
* Creates a dictionary where student names are keys and marks are values
* Asks the user to input student name
* Retrieves and displays the corresponding marks
"""


students = {
    "Alice": 85,
    "Shivani": 100,
    "Gouri": 92,
    "Khushi": 69,
    "Prateek":98
}

name = input("Enter student's name: ").lower()  # convert input to lowercase

found = False

for student in students:
    if student.lower() == name:
        print(f"{student}'s marks : {students[student]}")
        found = True
        break

if not found:
    print("Student not found.")