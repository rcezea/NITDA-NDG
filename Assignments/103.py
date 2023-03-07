#!/usr/bin/python3
"""
ASSIGNMENT
1. Use the os and os.path modules to list the contents of your Downloads folder,
and indicate for each item whether it's a file or a folder.
2. Display numbers from -10 to -1 using for loop
3. Given a list of numbers. Print only the even values.
4. Write a program to find the username of a person, which is the key in the
dictionary, and print the corresponding code. If the name of the person is not in
the dictionary, then telling me that the name is not found.
5. Find the largest item from a given list
6. Given an array arr[] of n elements, write a function to search a given element x
in arr[]
7. Write a function division() that accepts two arguments. The function should be
able to catch an exception such as ZeroDivisionError, ValueError, or any unknown
error you might come across when you are doing a division operation.
8. Using a slice, create a reversed copy of your list of favorite foods
"""

#Question2
'''
for i in range (-10, 0, 1):
    print(i)
'''
#QUestion3
'''
data = [2, 4, 6, 7, 9, 21, 45, 67,32, 80]
for i in data:
    if i % 2 == 0:
        print(i)
'''

#Question 4
"""
store = {"rcezea": "Richard", "rcflick": "Danteflick", "chimex": "Chiemerie", "akoii": "Simon"}
input = input("Enter a nickname: ")
if input in store:
    print(store[input])
else:
    print("Name not found")
"""

#Question 5
"""
data = [56, 49, 23, 21, 45, 67, 89, 90, 98, 84]
print(max(data))
"""

#Question 6
"""
x = input("What value do you want to search in the array: ")
data = ["me", "you", "boy", "girl"]
index = 0
for i in data:
    index += 1
    if i == x:
        print("{} was found at index {}".format(x, index - 1))
"""

#Question 7
"""
def division(a, b):
    try:
        print(a / b)
    except:
        print("An error occurred")

if __name__ == "main":
    x = input("Enter the numerator: ")
    y = input("Enter the denominator: ")
    division(x, y)
"""

#Question 8
food = ["rice", "beans", "chicken", "pizza", "wraps", "burgers", "sea food"]
print("Reserved list: ", food[-1:-7:-1])