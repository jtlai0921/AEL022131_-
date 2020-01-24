def mul(n) :
    if n < 1 :
        return 0
    else :
        return n*(n+1) + mul(n-1)
    
while True :
    n = eval(input('n = '))
    if n >= 2 and n <= 100 :
        break
    else :
        print('輸入資料不符, 請重新輸入...')

sum = mul(n)
i = 2
while i <= n :
    print((i-1)*i, end = ' + ' )
    i = i + 1
print ('%d = %d' %((i-1)*i, sum))