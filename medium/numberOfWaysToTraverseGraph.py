#kutty's Playground

def numberOfWaysToTraverseGraph(width, height):
    dp=[[0 for x in range(width)] for y in range(height)]
    dp[0][0]=1

    for i in range(height):
        for j in range(width):
            if i == 0 and j == 0:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]

width =4
height = 3
print(numberOfWaysToTraverseGraph(width, height))