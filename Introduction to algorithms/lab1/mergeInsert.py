def mergeInsert(list, key):
    n = len(list)
    topIndex = n
    bottomIndex = 0
    midPoint = topIndex // 2
    subListLength = topIndex - bottomIndex

    while subListLength > 0:
        if list[midPoint] == key:
            break
        elif list[midPoint] > key:
            topIndex = midPoint
            midPoint = bottomIndex + ((topIndex - bottomIndex) // 2)
            subListLength = topIndex - bottomIndex
        elif list[midPoint] <= key:
            bottomIndex = midPoint + 1
            midPoint = bottomIndex + ((topIndex - bottomIndex) // 2)
            subListLength = topIndex - bottomIndex

    list.insert(midPoint, key)
    return list