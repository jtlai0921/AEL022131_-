def G(n, x):
    if(x == 0):
        return 1
    else:
        return ((2*n)+2) * G(n, x-1)
    
for x in range(5):
    print (G(2, x))