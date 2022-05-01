#kutty's Playground

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]

    result = array[:]
    result[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        result[i] = max(result[i - 1], result[i - 2] + array[i])
    return result[-1]

array = [75,105,120,75,90,135]
print(maxSubsetSumNoAdjacent(array))