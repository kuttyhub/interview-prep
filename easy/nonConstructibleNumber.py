def nonConstructibleChange(coins):
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
    coinValue = 1
    while len(res)>0 and coinValue == res[0]:
        res.pop(0)
        coinValue+=1
    return coinValue

coins=[109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]
print(nonConstructibleChange(coins))