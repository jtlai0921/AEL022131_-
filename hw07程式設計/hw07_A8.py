def G(a):
    print(a, end = '  ')
    if (a >= 3):
        return
    else:
        G(a + 1)
    print(a, end = '  ')  
    
G(1)
