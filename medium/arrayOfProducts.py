#kutty's playground 

from functools import reduce


def arrayOfProducts(array):
    res =[]
    for i in range(len(array)):
        prod = getProduct(array[:i])*getProduct(array[i+1:])
        res.append(prod)

    return res

def getProduct (arr):
    if len(arr)==0:
        return 1
    return reduce(lambda x, y: x * y, arr)


array = [5,1,4,2]
result = arrayOfProducts(array)
print(result)