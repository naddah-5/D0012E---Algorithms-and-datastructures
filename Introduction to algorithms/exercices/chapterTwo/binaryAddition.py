from utils.dataGenerators.binaryArray import binaryArray

def binaryIntegerAdder(n):
    a = binaryArray(n)
    b = binaryArray(n)
    i = 0
    carry = 0
    result = []
    carryList = []
    while(i<n):
        temp = a[i] + b[i] + carry
        carryList.append(carry)
        if temp == 3:
            carry = 1
            result.append(1)
        elif temp == 2:
            carry = 1
            result.append(0)
        elif temp == 1:
            carry = 0
            result.append(1)
        else:
            result.append(0)
        i += 1
    result.append(carry)
    print("carry list =             ", carryList)
    print("integer a =              ", a)
    print("integer b =              ", b)
    print("resulting integer c =    ", result)
    return result

print(binaryIntegerAdder(10))