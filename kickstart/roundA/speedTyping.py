def checkCanVaid(validString,erroredString):
    #check valid string
    ptr1 = ptr2 =0
     
    while ptr1 < len(validString) and ptr2 <len(erroredString):
        if validString[ptr1]== erroredString[ptr2]:
            ptr1+=1
        ptr2+=1
    
    return "IMPOSSIBLE" if ptr1  != len(validString) else len(erroredString) - len(validString)




t= int(input())
for i in range(t):
    t1 = input()
    t2=input()
    print(checkCanVaid(t1,t2))


# t1 ="aaaa"
# t2="aaaaa"
# t3 ="bbbbb"
# t4="bbbbc"

t1="Ilovecoding"
t2="IIllovecoding"
t3="KickstartIsFun"
t4="kkickstartiisfun"

print(checkCanVaid(t1,t2))