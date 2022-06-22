def isRotatedString(s1,s2):
    k=0
    while s1[k] != s2[0]:
        k+=1
    s1 = s1[k:]+s1[:k]
    
    return s1 == s2

s1 = "waterbottle"
s2 = "erbottlewat"
print(isRotatedString(s1,s2))