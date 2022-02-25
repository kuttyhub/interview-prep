def sortedSquaredArray(array):
    res=[0 for _ in range(len(array))]
    smallIdx=0
    largeIdx=len(array)-1

    for idx in reversed(range(len(array))):
        small=array[smallIdx]
        large = array[largeIdx]
        if abs(small)>abs(large):
            res[idx]=small**2
            smallIdx+=1
        else:
            res[idx]=large**2
            largeIdx-=1
    return res

array=[-10, -5, 0, 5, 10]
print(sortedSquaredArray(array))