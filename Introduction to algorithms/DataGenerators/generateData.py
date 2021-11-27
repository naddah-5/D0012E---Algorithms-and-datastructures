from random import randrange;

## generates a integer list of the size specified by "size" and individual element values ranging between zero and "maxValue"
## allows for duplicate values
def generateData(size, maxValue):
    i = 0;
    inputData = [];
    while (i<size):
        inputData.append(randrange(maxValue));
        i = i+1;
    return inputData;