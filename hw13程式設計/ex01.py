import requests
from bs4 import BeautifulSoup
url = 'http://www.taiwanlottery.com.tw/index_new.aspx'
html = requests.get(url)
bs = BeautifulSoup(html.text, 'html.parser')
data1 = bs.select(".contents_box02") 
data2 = data1[2].find_all('div', {'class':'ball_tx'})

str1=""
print("本期大樂透開獎結果如下：")
for n in range(6,len(data2)):
    str1 += data2[n].text + " "
print("號碼順序：%s" %(str1))


    
red=data1[2].find('div', {'class':'ball_red'})#在第3個區塊中抓出紅球      
print("特別號碼：%s" %(red.text))
