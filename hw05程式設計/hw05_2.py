name = ['老張', '發叔', '李董', '豪哥', '小何']
age = [54, 46, 50, 40, 38]
ans = input('1. 由小到大排序   2. 由大到小排序 : ')
if ans == '1':
    print('由小到大排序:', end ='  ')
    for loop in range(1, 5):
        for index in range(0, (5-loop)):
            if age[index] > age[index+1]:
                aTemp = age[index]
                age[index] = age[index+1]
                age[index+1] = aTemp
                nTemp = name[index]
                name[index] = name[index+1]
                name[index+1] = nTemp
    for i in range(5):
        print('%s:%d' %(name[i], age[i]), end ='   ')
if ans == '2':
    print('由小到大排序:', end ='  ')
    for loop in range(1, 5):
        for index in range(0, (5-loop)):
            if age[index] < age[index+1]:
                aTemp = age[index]
                age[index] = age[index+1]
                age[index+1] = aTemp
                nTemp = name[index]
                name[index] = name[index+1]
                name[index+1] = nTemp
    for i in range(5):
        print('%s:%d' %(name[i], age[i]), end ='   ')         
            
