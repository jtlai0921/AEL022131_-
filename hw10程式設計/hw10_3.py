import os
#fPath = input('請輸入資料夾路徑：')
fPath = 'c:/stu101/'
if not os.path.exists(fPath):
    os.mkdir(fPath)

#fName = input('請輸入檔案名稱：')
fName = 'score.txt'
fFile = fPath + fName
if not os.path.exists(fFile):
    f = open(fFile, 'w+')
else:
    f = open(fFile, 'a+')

keyin = True
while keyin:
    yn = input('是否要輸入資料？(y/n)：')
    if yn == 'y' or yn == 'Y':
        str = input('輸入學生姓名,國文,英語成績：')
        f.write(str+'\n')
    else:
        keyin = False
       
f.seek(0)
print('\n姓名\t國文\t英語')
print('=========================')
for lines in f:
    lineStr = lines.strip()
    arr = lineStr.split(',')
    print('%s\t%s\t%s' %(arr[0],arr[1],arr[2]))
f.close()