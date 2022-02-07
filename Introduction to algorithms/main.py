from Algorithms.insertionSort import insertionSort
from Algorithms.bubbelSort import bubbelSort
from DataGenerators.integerArray import integerArray

c = 0;
while(c < 20):
    print("");
    c = c + 1;
inputData = integerArray(100, 100);
print("The input data is: ", inputData);
sortedData = bubbelSort(inputData);
print("The sorted data is: ", sortedData);