## takes a input and two integers as input, it then swaps the elements in the indecies indicated by the input
def swapElements(inputList, index_1, index_2):
    ## if the indecies are the same there is no need to manipulate the data
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
        ## if the indecies were entered in the wrong order simply call the function again with the correct order
        return swapElements(inputList, index_2, index_1);
