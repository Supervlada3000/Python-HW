#Дан список, найти в нем второй максимум
a = [1, 2, 3, 4, 5, 6, 7]
mx = max(a)
a.remove(mx)
print (max(a))