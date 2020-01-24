A = [[1,2,3], [4,5,6]]
B = [[1,2], [3,6], [4,2]]
C = [[0,0], [0,0]]

print('矩陣 A')
for i in range(2):
    for j in range(3):
        print(' %d ' %A[i][j], end='')
    print()

print()
print('矩陣 B')
for i in range(3):
    for j in range(2):
        print(' %d ' %B[i][j], end='')
    print()

for i in range(2):
    for j in range(2):
        C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + A[i][2]*B[2][j]


print()
print('矩陣A * 矩陣B')
for i in range(2):
      for j in range(2):
          print(' %d ' %C[i][j], end='')
      print()
    
