a = 1024
b = 7
while b%2!=0:
    a = a//10
    b = a-b
    while b < 80:
        break
a = a + 15
b = b - 80

print ("a = ", a, "b = ", b)

