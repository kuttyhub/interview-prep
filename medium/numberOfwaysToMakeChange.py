#Kutty's Playground

def numberOfWaysToMakeChange(n, denoms):
    dp=[0]*(n+1)
    dp[0]=1
    for denom in denoms:
        for i in range(1,n+1):
            if denom<=i:
                dp[i]+=dp[i-denom]
    print(dp)
    return dp[-1]

n = 10
demons = [1,5,10,25]
print(numberOfWaysToMakeChange(n, demons))
