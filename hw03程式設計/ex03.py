income=int(input('請輸入您的綜合所得淨額： '))
if (income<=540000): tax=0;
if ((income>540000) and (income<=1210000)): tax=0.12*income
if ((income>1210000) and (income<=2420000)): tax=0.2*income
if ((income>2420000) and (income<=4530000)): tax=0.3*income
if ((income>4530000) and (income<=10310000)): tax=0.4*income
if (income>10310000): tax=0.45*income
print('您所要繳交的所得稅額是： %.1f'%tax);