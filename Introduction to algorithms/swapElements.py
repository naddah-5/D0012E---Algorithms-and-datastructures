def swapElements(inputList, index_1, index_2):
    if(index_1 == index_2):
        return inputList;
    elif(index_1 < index_2):
        ##note that the order is important here since the .pop function removes the element from the list
        element_2 = inputList.pop(index_2);
        element_1 = inputList.pop(index_1);
        inputList.insert(index_1, element_2);
        inputList.insert(index_2, element_1);
        return inputList;
    else:
        return swapElements(inputList, index_2, index_1);
