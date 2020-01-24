mon=int(input('請輸入一個 1~12 之間的月份： '))
if (mon==3 or mon==4 or mon==5) :
    print('春天')
elif (mon==6 or mon==7 or mon==8) :
    print('夏天')
elif (mon==9 or mon==10 or mon==11) :
    print('秋天')
elif (mon==12 or mon==1 or mon==2) :
    print('冬天')
else:
    print('輸入錯誤！')