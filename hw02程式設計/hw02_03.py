i=int(input('請輸入整數值：'))
print('%d的資料型別為%s'%(i,type(i)))
f=float(input('請輸入浮點數值：'))
print('%f的資料型別為%s'%(f,type(f)))
b=bool(input('請輸入布林值：'))
print(b,'的資料型別為%s'%(type(b))) #因為布林值沒有對應的%型別字元
s=input('請輸入字串資料：')
print('%s的資料型別為%s'%(s,type(s)))
