def getNewNumber(number):
    if int(number)%9 ==0:
        return number[0]+"0"+number[1:]
    else:
        res=""
        newNumber = 9-(int(number)%9)
        for idx,val in enumerate(number):
            if newNumber <  int(val):
                res += str(newNumber) + number[idx:]
                break
            else:
                res+=val
        else:
            res+=str(newNumber)
        return res

t= int(input())
for i in range(1,t+1):
    n = input()
    print("Case #{}: {}".format(i,getNewNumber(n)))