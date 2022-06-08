def kSplit(list, k):
    sublists = []
    while len(list) > 0:
        if len(list) > k:
            sublists.append(list[:k])
            list = list[k:]
        elif len(list) > 0:
            sublists.append(list)
            list = []
    return sublists