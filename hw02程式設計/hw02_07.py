money=int(input('請輸入存款金額：(整數)'))
rate=float(input('請輸入年利率：(浮點數)'))
years=int(input('請輸入存款年數：(整數)'))
total=money+money*rate/100*years   #單利本利和，利率要除以100
print('單利：%d元%3d年的本利和 = %12.1f元'%(money, years, total))
total=money*(1+rate/100)**years   #複利本利和
print('複利：%d元%3d年的本利和 = %12.1f元'%(money, years, total))
