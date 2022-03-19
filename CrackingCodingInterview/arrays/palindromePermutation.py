def palindrome_permutation(string):
    #time complexcity O(n)
    #space complexity O(1) #atmost we have 26 unique alphabets only 

    string = string.replace(" ","")
    string = string.lower()
    frequencyTable = {}
    for i in string:
        frequencyTable[i] = frequencyTable.get(i,0)+1

    if len(string)%2==0:
        #if its even all characters should appear even times
        for i in frequencyTable.values():
            if i%2 != 0:
                return False
    else:
        #if its odd then only one character can appear odd but others charactes should be in even times
        first_ood_appeared = False
        for i in frequencyTable.values():
            if first_ood_appeared:
                #check all characters are even
                if i%2 != 0:
                    return False
            else:
                if i%2 != 0:
                    first_ood_appeared = True
    return True

string = "Tact Coa"

print(palindrome_permutation(string))