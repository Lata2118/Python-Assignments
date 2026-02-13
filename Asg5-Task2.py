""" ASSIGNMENT - 5
Task - 2 To demonstrate list slicing
A Python program that
* Creates a list of numbers from 1- 10
* Extracts the first five elements from the list
* Reverses these extracted elements
* Prints both the extracted list  and the reversed list
"""

l1=[1,2,3,4,5,6,7,8,9,10]
l2=(l1[0:5])

print(f"Original List : ", l1)
print(f"Extracted first five elements : " , l2 )
l2.reverse()
print(f"Reversed Extracted elements : ",l2)






