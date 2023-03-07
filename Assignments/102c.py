#!/usr/bin/python3

#program to check if a number is a factor of 10

number = int(input("Enter a number: "))
if 10 % number == 0:
    print("{} is a factor of {}".format(number, 10))
else:
    print("{} is not a factor of {}".format(number, 10))