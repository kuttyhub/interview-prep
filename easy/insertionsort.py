def insertionSort(array):
    for i in range(len(array)):
        key = array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key 

a = [8, 5, 2, 9, 5, 6, 3]
insertionSort(a)
print(a)