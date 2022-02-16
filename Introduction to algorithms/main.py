import os
import time

from algorithms.insertionSort import insertionSort
from algorithms.bubbelSort import bubbelSort
from utils.dataGenerators.integerArray import integerArray
from exercices.chapterTwo.binaryAddition import binaryIntegerAdder
from lab1.binarySearch import binarySortSearch

def sampleTime():
    timeSample = time.time()
    return timeSample

os.system('clear')
timeStamp = time.time()
A = integerArray(100, 20)
bubbelSort(A)
print(A)
B = binarySortSearch(A, 8)
print(B)

#print(sampleTime() - timeStamp)
#binaryIntegerAdder(10)
#print(sampleTime() - timeStamp)