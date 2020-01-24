def square(n) :
    if n <= 0 :
        return 0
    else :
        return n*n + square(n-1)
    
while True :
    n = eval(input('n = '))
    if n > 0 and n <= 10 :
        break
    else :
        print('輸入資料不符, 請重新輸入...')

sum = square(n)
while n > 1 :
    print(n*n, end = ' + ' )
    n = n-1
print('1 = %d' %sum )