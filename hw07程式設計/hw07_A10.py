def G(a, x):
    if(x == 0):
        return 1
    else:
        return (a * G(a, x-1))
    
print(G(3, 7))
    
