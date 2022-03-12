def bubbleSort(array):
    # Write your code here.
    while True:
        flag =True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                flag = False
                array[i+1],array[i] = array[i],array[i+1]
        if flag:
            return

a = [8, 5, 2, 9, 5, 6, 3]
bubbleSort(a)
print(a)