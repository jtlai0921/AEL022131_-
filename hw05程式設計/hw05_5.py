data = [['老張', '0911443300'], ['Mary', '0928000001'],
        ['發叔', '0431748484'], ['Tom', '0912345678'],
        ['李董', '0255111111'], ['豪哥', '0977229900'],
        ['小何', '0928888888']]
name = input('輸入查詢的姓名：')

find=False
for i in range(7):
    if data[i][0] == name:
        print('%s 的電話號碼為 %s ' %(name, data[i][1]))
        find=True
        break

if find==False:
    print('無 %s 的資料' %name)
    
