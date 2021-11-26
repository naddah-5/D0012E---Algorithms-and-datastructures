from swapElements import swapElements

def bubbelSort(inputData):
    loopCounter = 0;
    while(loopCounter < len(inputData)):
        i = 0;
        while(i < len(inputData)-1):
            if(inputData[i] > inputData[i+1]):
                inputData = swapElements(inputData, i, i+1)
                i = i + 1;
            else:
                i = i + 1;
        loopCounter = loopCounter + 1;
    return inputData;