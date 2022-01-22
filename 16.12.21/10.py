#Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
d = {}
n = int(input())
for i in range (n):
    country = input()
    cities = input().split()
    for city in cities:
        d[city] = country
print(d)