#!/usr/bin/python3

#program to print even numbers from input to 100

number = int(input( 'Enter a number less than 100: '))
if number >= 100:
    exit (0)
for i in range(number, 100):
    if i % 2 == 0:
        print(i)
