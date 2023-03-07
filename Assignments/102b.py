#!/usr/bin/python3

#program to check if a number is positive or negative

number = int(input("Enter a number: "))
if number == 0:
    print("positive")
elif number/abs(number) == 1:
    print("positive")
elif number/abs(number) == -1:
    print("negative")