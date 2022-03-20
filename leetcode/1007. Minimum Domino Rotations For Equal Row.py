
from typing import DefaultDict, List


def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
    topFreqeuncy ,bottomFrequency , same =DefaultDict(int),DefaultDict(int),DefaultDict(int)
    
    for (top,bottom) in zip(tops,bottoms):
        topFreqeuncy[top] +=1 
        bottomFrequency[bottom] +=1
        if top == bottom:
            same[top] +=1

    #because 1 -6 distinct value we only have
    for i in range(7):
        if topFreqeuncy[i]+bottomFrequency[i] - same[i] == len(tops):
            return len(tops) - max(topFreqeuncy[i],bottomFrequency[i])
    
    return -1
            
tops=[2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
print(minDominoRotations(tops,bottoms))