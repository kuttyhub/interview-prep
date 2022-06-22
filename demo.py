bank=[]
amount = input().split()
for i in amount: 
    bank.append(list(map(int,i.split())))
amount = int(input())
bank = [[500,2],[100,10],[50,10],[20,10],[5,10]]
notes = {
    500:2,
    100:10,
    50:10,
    20:10,
    5:10
}
amount =1745
result  = []
for k,v in sorted(notes.items(),reverse=True):
    if amount>=k:
        j = min(v,amount //k)
        amount -= j*k
        result.append(f"{k}*{j}")
result = " + ".join(result)
print(result)


