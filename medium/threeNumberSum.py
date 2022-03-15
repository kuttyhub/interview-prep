#kuttys playground

from turtle import right


def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    res=[]
    n=len(array)
    for i in range(n-2):
        left = i+1
        right = n-1
        while left<right:
            currentsum = array[i]+array[left]+array[right]
            if currentsum == targetSum:
                res.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif currentsum< targetSum:
                left+=1
            else:
                right-=1
    return res

array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array,targetSum))