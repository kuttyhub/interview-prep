#kutty playground

def isMonotonic(array):
    n= len(array)
    if n <1:
        return True
    isIncreasing = True if array[0]<=array[1] and array[0]>0 else False
    i=2
    while i<n:
        if isIncreasing :
            if  array[i-1]>array[i]:
                return False
        else :
            if array[i-1]<array[i]:
                return False
        i+=1
    return True




# arr = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
arr =[1, 5, 10, 1100, 1101, 1102, 9001]

print(isMonotonic(arr))