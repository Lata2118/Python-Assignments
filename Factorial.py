"""
Assignment - 3
Task 1
A Python program to calculate the factorial of a number without recursion
"""
# without recursion
num=int(input("Enter a number: "))
factorial=1

if num>0:
    for i in range(1,num+1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")
