#Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что f_n = A. Если А не является числом Фибоначчи, выведите число -1.
c = int(input())
f1 = 1
f2 = 1
a = [1, 1]
i = 0
while i < 15:
    f_sum = f1 + f2
    f1 = f2
    f2 = f_sum
    a.append(f2)
    i = i + 1
q = 0
for i in range (len(a)):
    if c == a[i]:
        print (i+1)
        q += 1
if q == 0:
    print ('-1')