lastTime=input('請輸入前一次遊戲過關編號：')
thisTime=input('請輸入這一次遊戲過關編號：')
#字串資料要用int()函式轉型為整數，才能進行四則運算
#數值資料要轉型為字串，才能用+運算子來做字串連接
print('恭喜過了 '+str(int(thisTime)-int(lastTime))+' 關！')
