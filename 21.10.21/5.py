#Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
a = [1, 2, 3, 2, 3, 4, 3, 4, 5, 6]
for i in range(len(a)):
    c = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            c+=1
    if c == 1:
        print (a[i])
