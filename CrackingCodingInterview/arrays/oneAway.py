

def one_away(string,result):
    m,n = len(string),len(result)
    dp = [[0 for i in range(n+1)]for j in range(m+1)]

    for i in range(n):
        dp[0][i] = i

    for i in range(m):
        dp[i][0] = i
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if string[i-1] == result[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] =1+ min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    
    return dp[m][n] == 1 

# string = "pale"
# result = "pal"
# string = "pale"
# result = "bale"
string = "pale"
result = "bake"

print(one_away(string,result))