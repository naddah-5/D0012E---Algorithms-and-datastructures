from random import randrange;

def binaryArray(size):
    i = 0
    inputData = []
    while (i<size):
        ## generates a integer n such that, 0 =< n < 2
        inputData.append(randrange(2))
        i = i+1
    return inputData