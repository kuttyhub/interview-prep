#kutty's playground

def longestPeak(array):
    largestPeak = 0
    n=len(array)
    i = 1
    while i<n-1:
        isPeek = array[i-1]<array[i] and array[i]>array[i+1]
        if not isPeek:
            i+=1
            continue
        leftIdx = i-2
        rightIdx = i+2

        #travese to leftside to find last element
        while leftIdx>=0 and array[leftIdx]<array[leftIdx+1]:
            leftIdx-=1

        #travesing to rightside to find last element
        while rightIdx < n and array[rightIdx-1]>array[rightIdx]:
            rightIdx+=1
        
        #get distance and set it
        distance = rightIdx - leftIdx - 1
        largestPeak = max(largestPeak,distance)

        i=rightIdx
    return largestPeak

arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(arr))