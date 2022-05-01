
def twoSum(array,target):
    dict = {}
    for i in array:
        reminder = target - i
        if dict.get(i) is not None:
            return [dict[i],i]
        else:
            dict[reminder] = i
    return []


def threeSum(array,target):

    for i in array:
        subTarget = target-i 
        twoSum = twoSum(array, subTarget)
        if (len(twoSum) ==2):
            return [i]+twoSum

    return None



    # for i in array:
    #     for j in array:
    #         for k in array:
    #             if i+j+k == target: O(n^3)

    # for i in array:
    #     for j in array:
    #         rem = target - (i+j) 
    #         if  ren in array: 
    #             return i+j +(target - (i+j))

array =[1,2,3,4,5]
k = 9 (1,3,5)

print(twoSum(array,k))

