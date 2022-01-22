#Даные два вектора (списка), вычислить скалярное произведение
a = input().split()
b = input().split()
c = 0
for i in range (len(a)):
    c += int(a[i])*int(b[i])
print(c)