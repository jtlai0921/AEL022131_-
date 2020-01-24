sub = ['Dog','Cat','Pig','Monkey','Elephant']
ver = ['runs','walks','jumps']
adv = ['quickly','slowly']
import random as R
for i in range(5):
    r1 = R.randint(0,4)
    r2 = R.randint(0,2)
    r3 = R.randint(0,1)
    print('%s %s %s.' %(sub[r1],ver[r2],adv[r3]))
