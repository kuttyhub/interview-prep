def twoNumberSum(array, targetSum):
    t={}
    for i in array:
        if t.get(i) is not None:
            return [i,t[i]]
        else:
            t[targetSum-i]=i
    return [] 
   
arr=[3,5,-4,8,11,1,-1,6]
target=10
print(twoNumberSum(arr,target))
