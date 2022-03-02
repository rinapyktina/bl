a = 7
bbb = [2] * a
for i in range(a):
    bbb[i] = [2]*a

for i in range(a):
    bbb[i][2] = bbb[i][2]*2
for i in range(a):
    bbb[5][i] = bbb[5][i] + 3*i

print(bbb[5][2])