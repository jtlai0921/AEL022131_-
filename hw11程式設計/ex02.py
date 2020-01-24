import matplotlib.pyplot as plt

font = {'family' : 'DFKai-SB'}  
plt.rc('font', **font)


listPercent = [25.2, 31.8, 43]
listBooks = ['商管', '資電', '設計']
listColors = ['red', 'pink', 'yellow']
listExplode=(0, 0, 0.1)

plt.pie(listPercent, shadow=True , labels=listBooks,
        colors=listColors, explode=listExplode, labeldistance=1.1,
        autopct='%3.1f%%', pctdistance=0.6, startangle=0)

plt.title('碁峰科大招生員額比例')
plt.axis('equal')
plt.legend()
plt.show()