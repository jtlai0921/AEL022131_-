def F(n):
    global m
    sum = 0
    if n < 2:
        return 0
    for k in range(1, n+1):
        sum = sum + k
        m=m+1
    sum = sum + F(int(2*n/3))
    return sum

m=0
F(1000) 
print(m)