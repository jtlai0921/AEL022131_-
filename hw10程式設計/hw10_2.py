fName1 = 'poem1.txt'
fName2 = 'poem2.txt'
fName3 = 'poem3.txt'
try:
    fIn1 = open(fName1, 'r')
    str1 = fIn1.read()
    fIn2 = open(fName2, 'r')
    str2 = fIn2.read()
    fOut = open(fName3, 'w')
    fOut.write(str1)
    fOut.write('\n\n')
    fOut.write(str2)
    fIn1.close()
    fIn2.close()
    fOut.close()
except FileNotFoundError:
    print('檔案處理有誤!!')