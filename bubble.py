#!/usr/bin/python3

# Example 1:
def Bubble(data):
    swap = True
    while swap:
        swap = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i+1] = data[i + 1], data[i]
                swap = True


if __name__ == "__main__":
    data = [7, 8, 6, 54, 34, 2, 1, 3, 1]
    print("Unsorted: ", data)
    Bubble(data)
    print("Sorted: ", data)
'''

'''
# Example 2
def heap(data, n):
    if n == 1:
        print(data)
        return
    for i in range(n):
        heap(data, n - 1)
        if n % 2 == 0:
            data[i], data[n - 1] = data[n - 1], data[i]
        else:
            data[0], data[n - 1] = data[n - 1], data[0]


if __name__ == "__main__":
    data = [7, 6, 8]
    print("Unsorted: ", data)
    heap(data, n=len(data))


# example 3
import requests

url = requests.get("http://www.google.com")
print(url)