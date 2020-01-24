import tkinter as tk
from tkinter import messagebox as msgbox

def fnOk():
    vMoney = money.get()
    vRate = rate.get()
    if change.get()==0:
        result = '台幣{0}元可兌換成美金{1}元'.format(vMoney, round(vMoney/vRate,2))
    else:
        result = '美金{0}元可兌換成台幣{1}元'.format(vMoney, (vMoney*vRate)) 
    msgbox.showinfo("台幣和美金相互兌換", result)

win = tk.Tk()
win.title('台幣和美金相互兌換')
win.geometry('280x150')

money=tk.IntVar()   

rate = tk.DoubleVar()

lblMoney = tk.Label(win, text='請輸入金額', padx=10, pady=8)
lblMoney.grid(row=0, column=0)

txtMoney = tk.Entry(win, width=15, textvariable=money)
txtMoney.grid(row=0, column=1)

lblRate = tk.Label(win, text='請輸入美金匯率', padx=10, pady=8)
lblRate.grid(row=1, column=0)

txtRate = tk.Entry(win, width=15, textvariable=rate)
txtRate.grid(row=1, column=1)

change=tk.IntVar()
change.set(0)
radNTTOUS = tk.Radiobutton(win, text='台幣換美金', variable=change ,value=0 , padx=10, pady=8);
radNTTOUS.grid(row=2, column=0)
radUSTONT = tk.Radiobutton(win, text='美金換台幣', variable=change ,value=1 , padx=10, pady=8);
radUSTONT.grid(row=2, column=1)

btnOk = tk.Button(win, text='兌換', command=fnOk )
btnOk.grid(row=3, column=0)

win.mainloop()

