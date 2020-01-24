while True:
    try:
        n1 = int(input('輸入被除數： '))
    except ValueError:
        print('輸入錯誤, 請輸入整數')
        continue
       
    break    

while True:
    try:
        n2 = int(input('輸入除數： '))
        n3 = float(n1 / n2)
    except ValueError:
        print('輸入錯誤, 請重新輸入')
        continue
    except ZeroDivisionError:
        print('除數為0, 請重新輸入')
        continue
       
    print('%d / %d = %.2f' %(n1,n2,n3))
    break    