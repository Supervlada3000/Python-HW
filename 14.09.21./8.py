#Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента.
a = []
c = 1
z = 0
while c != 0:
    c = int(input())
    a.append(c)
for j in range (len(a)-1):
    if a[j] < a[j + 1]:
        z += 1
print (z)