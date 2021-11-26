from insertionSort import insertionSort
from bubbelSort import bubbelSort
from generateData import generateData

c = 0;
while(c < 20):
    print("");
    c = c + 1;
inputData = generateData(10, 100);
print("The input data is: ", inputData);
sortedData = bubbelSort(inputData);
print("The sorted data is: ", sortedData);