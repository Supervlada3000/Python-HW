#Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
a = []
c = 1
z = 0
while c != 0:
    c = int(input())
    a.append(c)
for j in range (len(a)-1):
    if a[j] < a[j + 1] > a[j + 2]:
        z += 1
print (z)
