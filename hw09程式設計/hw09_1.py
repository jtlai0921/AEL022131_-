def menu():
    print('=' * 40)
    print('\t 1.新增/修改字典')
    print('\t 2.刪除字典')
    print('\t 3.單字查詢')
    print('\t 4.結束程式')
    print('\t 請輸入選項(1～4)')

dict1 = {'cat':'貓','dog':'狗'}
while (1):
    menu()
    c = input()
    if(c == '4'):
        break
    elif(c == '1'):
        k = input('請輸入英文單字')
        v = input('請輸入中文解釋')
        dict1[k] = v
    elif(c == '2'):
        k = input('刪除哪個單字？')
        if(k in dict1):
            del dict1[k]
        else:
            print('不存在字典中')
    elif(c == '3'):
        k = input('查詢哪個單字？')
        if(k in dict1):
            print('%s 中文解釋 %s' %( k, dict1.get(k)))
        else:
            print('不存在字典中')
    else:
        print('請輸入選項(1～4)')
