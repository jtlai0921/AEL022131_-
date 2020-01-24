dict1 = {}
str = input()
for x in str:
    if(x in dict1):
        dict1[x] += 1
    else:
        dict1[x] = 1
list1 = dict1.keys()
for x in list1:
    print('%s 共使用%d次' %(x, dict1[x]))
