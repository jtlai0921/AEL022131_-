import matplotlib.pyplot as plt
font = {'family' : 'DFKai-SB'}  
plt.rc('font', **font)

listX = [2015, 2016, 2017, 2018, 2019, 2020]

listY1 = [500, 512, 430, 480, 490, 530]
plt.plot(listX, listY1, color='blue', ls='--',lw=4, label="商管")

listY2 = [430, 500, 510, 300, 320, 520]
plt.plot(listX, listY2, color='red', ls='-',lw=4, label="設計")

listY3 = [330, 400, 410, 500, 520, 580]
plt.plot(listX, listY3, color='green', ls=':',lw=4, label="資電")

plt.title("碁峰科大歷年招生錄取分數")
plt.ylim(0, 700)
plt.xlabel('年度')
plt.ylabel('分數')
plt.legend()
plt.show()