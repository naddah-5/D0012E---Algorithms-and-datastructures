def insertionSort(inputData):
    print("The raw input data is: ", inputData);
    sortedData = [];
        
    while (len(inputData) > 0):
        print(sortedData);
        i = 0;
        newElement = inputData.pop(0);
        if(len(sortedData) == 0):
            sortedData.insert(0, newElement);
        else:
            while(i < len(sortedData)):
                if(newElement < sortedData[i]):
                    sortedData.insert(i, newElement)
                    break
                elif(i == len(sortedData)-1):
                    sortedData.append(newElement);
                    break
                else:
                    i = i + 1;

    print("The sorted data is: ", sortedData);