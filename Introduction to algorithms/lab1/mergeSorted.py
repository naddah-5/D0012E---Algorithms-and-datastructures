from heapq import merge


def mergeSorted(listA, listB):
    mergedList = []
    while len(listA) and len(listB) > 0:
        if listA[0] < listB[0]:
            mergedList.append(listA.pop(0))
        else:
            mergedList.append(listB.pop(0))
    if len(listA) == 0:
        mergedList.extend(listB)
    else:
        mergedList.extend(listA)
    return mergedList