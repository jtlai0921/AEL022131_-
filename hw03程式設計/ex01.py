num=int(input('請輸入一個非零的整數： '))
if (num>0) :
    if (num % 2 == 0) : 
        data='正偶數' 
    else :
        data='正奇數' 
else :
    if (num % 2 == 0) : 
        data='負偶數'
    else :
        data='負奇數' 
print('所輸入的整數為 ' + data) 