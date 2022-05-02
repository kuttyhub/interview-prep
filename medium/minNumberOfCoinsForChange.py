#Kutty's Playground

def minNumberOfCoinsForChange(n, denoms):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for denom in denoms:
        for i in range(1, n + 1):
            if denom <= i:
                dp[i] = min(dp[i], dp[i - denom] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1
    


target = 11
denoms = [5]
print(minNumberOfCoinsForChange(target, denoms))