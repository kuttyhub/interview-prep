#Kutty's Playground
def kadanesAlgorithm(array):
    result = array[0]
    prev = array[0]

    for i in range(1,len(array)):
        prev = max(prev+array[i],array[i])
        result = max(result,prev)
    return result

array= [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(array))