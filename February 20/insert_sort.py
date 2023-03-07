#!/usr/bin/python3
def insert(arr):
    if len(arr) < 2:
        print(arr)
        return
    for i in range(len(arr)):
        count = 0
        while count < len(arr):
            x = arr[count]
            y = arr[count+1]
            if x > y:
                tmp = x
                arr[count + 1] = x
                arr[count] = y
            count += 1
            if count == (len(arr) - 1): break;
    print(arr)

#data = input("Enter a list of numbers: ").split()
#data = [int(x) for x in data]
data = [1, 2, 3, 4, 6, 1, 2, 3, 4, 6, 1, 2, 3, 4, 6, 1, 2, 3, 4, 6, 1, 2, 3, 4, 6, 1, 2, 3, 4, 6,1, 2, 3, 4, 6, 1, 2, 3, 4, 6]
insert(data)