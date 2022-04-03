    
import array
from ast import If
from ctypes import Array
# from distutils.spawn import spawn
# from enum import unique
# from re import U
from tkinter.tix import PopupMenu


def lonelyInteger(arr):
    spam = []

    # take spam and unique both value to compare with ----- spam array
    deepFiltring = []
    uniqueResult = []
    for i in range(len(arr)):
        popped = arr.pop()
        if popped not in arr:
            deepFiltring.append(popped)
        else:
            spam.append(popped)

    # compare deepFiltring array with spam array and give final result (unique result)
    for i in deepFiltring:
        if i not in spam:
            uniqueResult.append(int(i))

    for i in uniqueResult:
        print(i)



b = "18 49 15 30 56 20 49 67 82 69 84 63 93 87 66 17 38 32 17 32 94 66 67 63 48 64 84 82 87 18 79 64 79 15 71 94 59 5 22 59 4 98 81 4 98 73 69 88 30 81 48 56 71 20 93 22 73 5 88"
b = b.split(" ")
a = [4, 9, 95, 93, 57, 4, 57, 93, 9]



lonelyInteger(b)

