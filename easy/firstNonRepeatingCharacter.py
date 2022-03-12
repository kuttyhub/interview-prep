from collections import Counter
def firstNonRepeatingCharacter(string):
    # Write your code here.
    dic = dict(Counter(string))
    for  i in range(len(string)):
        if dic[string[i]] == 1:
            return i
    return -1

string = "abcdcaf"
print(firstNonRepeatingCharacter(string))