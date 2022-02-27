from array import array


def nonConstructibleChangeBruteForce(coins):
    #brute force method
    coins.sort()
    print(coins)
    res = set()

    for i in coins:
        temp=set()
        temp.add(i)
        for j in res:
            temp.add(i+j)
        res=set.union(res,temp)
    res = sorted(list(res))
    print(res)
    # array = [1, 1, 2, 3, 5, 7, 22]
    # {1}
    # {1, 2}
    # {1, 2, 3, 4}
    # {1, 2, 3, 4, 5, 6, 7}
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
    # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41}
    coinValue = 1
    while len(res)>0 and coinValue == res[0]:
        res.pop(0)
        coinValue+=1
    return coinValue

def nonConstructibleChange(coins):
    #optimal way
    coins.sort()
    currenMaxChange =0
    for i in coins:
        if currenMaxChange+1 >=i:
            currenMaxChange+=i
        else:
            return currenMaxChange+1
    return currenMaxChange+1
 

coins=[109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]
print(nonConstructibleChange(coins))