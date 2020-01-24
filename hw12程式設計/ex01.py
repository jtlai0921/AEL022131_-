import tkinter as tk

#定義fnOk函式，當按下確定鈕會執行此函式
def fnOk():
    vMoney = money.get()
    vRate=rate.get()/100
    interest=vMoney*vRate
    lblResult['text'] = '利息是{0}元'.format(interest)

win = tk.Tk()
win.title('銀行利息計算')
win.geometry('180x120')

money=tk.IntVar()   

rate = tk.DoubleVar()

lblMoney = tk.Label(win, text='本金', padx=10, pady=8)
lblMoney.grid(row=0, column=0)

txtMoney = tk.Entry(win, width=15, textvariable=money)
txtMoney.grid(row=0, column=1)

lblRate = tk.Label(win, text='年利率', padx=10, pady=8)
lblRate.grid(row=1, column=0)

txtRate = tk.Entry(win, width=15, textvariable=rate)
txtRate.grid(row=1, column=1)

btnOk = tk.Button(win, text='確定', command=fnOk )
btnOk.grid(row=2, column=0)

lblResult = tk.Label(win, text='', padx=10, pady=8)
lblResult.grid(row=2, column=1)
win.mainloop()

