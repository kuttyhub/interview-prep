def selectionSort(array):
    sortedIdx = 0
    while sortedIdx <len(array):
        #travese the list to find the smallest one
        smallestKeyIdx = sortedIdx
        for i in range(sortedIdx+1,len(array)):
            if array[smallestKeyIdx] > array[i]:
                smallestKeyIdx=i
        array[sortedIdx],array[smallestKeyIdx]= array[smallestKeyIdx],array[sortedIdx]
        sortedIdx+=1
    


a=  [8, 5, 2, 9, 5, 6, 3]
selectionSort(a)
print(a)