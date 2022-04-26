def rotate_matrix(matrix):
    res =[]
    n = len(matrix)
    for i in range(n):
        temp = []
        for j in range(n):
            temp.insert(0,matrix[j][i])
        res.append(temp)
    print(res)

n = 5
array =[]

k =1
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(k)
        k+=1
    array.append(temp)
rotate_matrix(array)