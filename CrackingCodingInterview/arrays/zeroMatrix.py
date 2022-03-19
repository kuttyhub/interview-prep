from array import array

#create m * n with initial value of zeros

def zero_matrix(m,n):
    #time O(m^n)
    #space O(mn)
    array =[[0 for i in range(n)] for i in range(m)]
    return array

m=3
n=2
print(zero_matrix(m,n))