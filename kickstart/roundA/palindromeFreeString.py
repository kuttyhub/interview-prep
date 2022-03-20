from itertools import combinations
import math


def checkPallindrome(string):
    return string == string[::-1]

def createPalindromeFreeString(string):
    if len(string)<=5:
        return "POSSIBLE"
    countOfReplace= string.count("?")
    print(countOfReplace)
    for i in  range(2**countOfReplace):
        combination=bin(i).replace("0b", "").zfill(countOfReplace)
        temp = string
        res = ""
        idx= 0
        for i in temp:
            if i == "?":
                res +=combination[idx]
                idx+=1
            else:
                res+=i
        print(res)
        print(checkPallindrome(res))




# if __name__ == "__main__":
#     t= int(input())
#     for i in range(1,t+1):
#         n=int(input())
#         # if checkPallindrome(input()):
#         #     print("Case #{}: POSSIBLE".format(i))
#         # else:
#         #     print("Case #{}: IMPOSSIBLE".format(i))
#         createPalindromeFreeString(input())

string = "100???001"
createPalindromeFreeString(string)