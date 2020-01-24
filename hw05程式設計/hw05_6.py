P = [0 for x in range(10)]
over=False
while over == False:
    print()
    print('未簽到座號:', end = ' ')
    over = True
    for i in range(10):
        if P[i] == 0:
            print(' %d ' %(i+1), end='')
            over = False
    if over == True:
        print('沒有, 全員到齊!')
        break

    print()
    num = eval(input('請輸入座號(1~10) : '))
    for j in range(10):
        if num == j+1:
            P[j] = 1
            break
