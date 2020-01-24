from random import randint

while (1):
    x = randint(0,1)
    y = randint(0,1)
    print(x, y, sep=' ; ')
    if x + y == 1:
        break
print('你擲出了聖筊')
