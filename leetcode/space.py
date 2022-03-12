import copy

p=20

q=60

n=3

 

# alien_lives=[80,80,120]

# golds=[100,200,300]

arr=[

    [80,100],

    [80,200],

    [120,300]

]

# p=50

# q=400

# n=2

# arr=[

#     [60,100],

#     [190,200]

# ]

 

# p=200

# q=10

# n=5

# arr=[

#     [20,100],

#     [30,20],

#     [20,101],

#     [200,500],

#     [10,1000]

# ]

 

maxGold = 0

 

def hit(aliens, goldObtained, isAshaTurn):
    global maxGold
    if len(aliens)==0:
        maxGold=max(maxGold,goldObtained)
        return

    temp = copy.deepcopy(aliens)

    temp[0][0] -= q
    if temp[0][0]<1:
        temp.pop(0)

    hit(temp,goldObtained,True)

    if isAshaTurn:
        for i in range(len(aliens)):
            temp=copy.deepcopy(aliens)
            temp[i][0]-=p
            
            if temp[i][0]<1:

                goldObtained+=temp[i][1]

                temp.pop(i)

            hit(temp,goldObtained,False)

 

hit(arr,0,True)

print(maxGold)