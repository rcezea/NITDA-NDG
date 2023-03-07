print("Assignment 3")
print("-------------------------------------------")
# use the range function to create a program that does the following
# Print out the numbers 0 to 9 inclusively
for i in range(10):
    print(i)
# Print out the numbers -5 to 5 inclusively
for i in range(-5,6):
    print(i)
# Print the even numbers between 50 and 80
for i in range(51,80):
    if (i % 2) == 0:
        print(i)
# Count down for a rocket take off 10, 9, 8,...1 ending with "blast off"
for i in range(10,0,-1):
    print(i)
print("blast off")
print("-------------------------------------------")