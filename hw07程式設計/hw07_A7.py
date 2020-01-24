def Mystery(x):
    if (x <= 1):
        return x
    else:
        return Mystery(x-2) + Mystery(x-1)
    
print (Mystery(9))