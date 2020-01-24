def comp(vm, vy, vr):
    return vm*pow(1+vr/12, vy*12)

print('== 複利率本利和試算 ==')
money = eval(input(' 請輸入本金：'))
rate = eval(input(' 請輸入年利率(％)：'))
year = eval(input(' 幾年後領回：'))
perRate = rate/100
print()
print('*** %d年後領回本利和：%d' %(year, comp(money,year,perRate)))
