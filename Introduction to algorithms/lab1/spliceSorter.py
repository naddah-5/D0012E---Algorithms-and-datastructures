from .kSplit import kSplit
from .bSort import bSort
from .mergeSorted import mergeSorted

def spliceBSort(list, k):
    splicedList = kSplit(list, k)
    i = 0
    while i < len(splicedList):
        splicedList[i] = bSort(splicedList[i])
        i += 1
    sortedList = []
    while len(splicedList) > 2:
        sortedList = mergeSorted(sortedList, splicedList.pop(0))

    return sortedList