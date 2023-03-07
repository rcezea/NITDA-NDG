#!/usr/bin/python3
import pyttsx3

with open("Mytext.txt", "w", encoding="utf-8") as f:
    f.write("hey there richard why would you say i am not working are you okay or wha!")

book = open(r"Mytext.txt")
book_txt = book.readlines()
read = pyttsx3.init()

for i in book_txt:
    read.say(i)
    read.runAndWait()