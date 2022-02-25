def isValidSubsequence(array, sequence):
    for i in array:
        if i == sequence[0] and len(sequence)>0:
            sequence.pop(0)
    return len(sequence)==0

array=[5,1,22,25,6,-1,8,10]
sequence=[1,6,-1,10]

print(isValidSubsequence(array=array,sequence=sequence))