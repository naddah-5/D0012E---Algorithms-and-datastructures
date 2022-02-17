import os
import time

from algorithms.insertionSort import insertionSort
from algorithms.bubbelSort import bubbelSort
from utils.dataGenerators.integerArray import integerArray
from exercices.chapterTwo.binaryAddition import binaryIntegerAdder
from lab1.bSort import bSort
from lab1.kSplit import kSplit
from lab1.spliceSorter import spliceBSort

def sampleTime():
    timeSample = time.time()
    return timeSample

os.system('clear')
timeStamp = time.time()
A = integerArray(10000, 10)
B = spliceBSort(A, 100)
print(B)
print(sampleTime() - timeStamp)

#print(sampleTime() - timeStamp)
#binaryIntegerAdder(10)
#print(sampleTime() - timeStamp)