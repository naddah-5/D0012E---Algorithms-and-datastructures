from random import randrange;

## generates a integer list of the size specified by "size" and individual element values ranging between zero and "maxValue"
## allows for duplicate values
def integerArray(size, maxValue):
    i = 0;
    inputData = [];
    while (i<size):
        ## randrange returns a pseudo-random integer between zero and the input integer
        ## note that this does include zero but not the max value, e.g. 0 <= random number < maxValue
        inputData.append(randrange(maxValue));
        i = i+1;
    return inputData;