from mergeInsert import mergeInsert
from random import randrange;


def integerArray(size, maxValue):
    i = 0
    inputData = []
    while (i<size):
        inputData.append(randrange(maxValue))
        i = i+1
    return inputData

def bSort(list):
    sortedList = []
    while len(list) > 0:
        x = list.pop(0)
        sortedList = mergeInsert(sortedList, x)
    return sortedList

A = integerArray(100, 10)
print(A)
print(bSort(A))