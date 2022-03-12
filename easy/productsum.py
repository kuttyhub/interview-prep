# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
s=0
def productSum(array,depth = 1):
    s=0
    for i in array:
        if type(i) == list:
            s+=productSum(i,depth+1)
        else:
            s+=i
    return depth*s



# arr =  [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
arr = [9, [2, -3, 4], 1, [1, 1, [1, 1, 1]], [[[[3, 4, 1]]], 8], [1, 2, 3, 4, 5, [6, 7], -7], [1, [2, 3, [4, 5]], [6, 0, [7, 0, -8]], -7], [1, -3, 2, [1, -3, 2, [1, -3, 2], [1, -3, 2, [1, -3, 2]], [1, -3, 2]]], -3]
print(productSum(arr))