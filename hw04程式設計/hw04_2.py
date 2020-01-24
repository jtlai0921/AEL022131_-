while (1):
    print('=== 主功能表 ===')
    print('1. 新增作業')
    print('2. 修改作業')
    print('3. 查詢作業')
    print('0. 結束程式')
    c = input('請輸入選項(0～3)：')
    if c == '1':
        print('新增作業…')
        continue
    if c == '2':
        print('修改作業…')
        continue
    if c == '3':
        print('查詢作業…')
        continue
    if c == '0':
        print('結束程式！')
        break
    print('輸入值不正確')
