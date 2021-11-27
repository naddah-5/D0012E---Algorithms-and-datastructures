from random import randrange;

def generateData(size, maxValue):
    i = 0;
    inputData = [];
    while (i<size):
        inputData.append(randrange(maxValue));
        i = i+1;
    return inputData;