def A(n, m):
    if (n < 10):
        if (m < 10):
            return n + m
        else:
            return A(n, m-2) + m
    else:
        return A(n-1, m) + n
    
print(A(13, 15))