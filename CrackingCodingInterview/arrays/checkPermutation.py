#Given two strings, write a method to decide if one is a permutation of the other.
from collections import Counter

def check_permutation(string1,string2):

    if len(string1)!= len(string2):return False
    hashTable = {}
    for i in string1:
        hashTable[i] = hashTable.get(i,0)+1
    
    for i in string2:
        if hashTable.get(i) is not None:
            hashTable[i] -=1
            if hashTable[i]<0:
                return False
        else:
            return False
            
    return True

def check_permutation_with_build_in_function(string1,string2):

    if len(string1) > len(string2):
        return False

    count1 = Counter(string1)
    count2 = Counter(string2)

    result = dict(count2-count1)
    if result:
        return False
    else:
        return True


string1 = "abc"
string2 = "cbaa"
print(check_permutation(string1,string2))