dist = float(input('請輸入距離(單位公尺)：')) #使用float()函式轉成浮點數，來提高精準度
sec = float(input('請輸入成績(單位秒)：'))
speed = (dist / 100) / (sec / 60) #距離/100為百公尺，秒數/60為分鐘
print('速度為：%.2f 百公尺/分鐘'%(speed))
