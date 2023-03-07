print("Assignment 1")
print("-------------------------------------------")
numbers = [14,22,0,-7,12,6]
# Print the first number in the list
print(numbers[0])
# Print the last number in the list
print(numbers[-1])
# Print the fourth number in the list
print(numbers[3])
# Print the list with only the first 2 numbers
print(numbers[:2])
# Print the list with only the last 3 numbers
print(numbers[-3:])
# Print the list starting at second element and ending including the fourth element
print(numbers[1:4])
# Print the list with all the even indicies
new = []
for i, j in enumerate(numbers):
    if i % 2 == 0:
        new.append(j)
print(new)
print("-------------------------------------------")