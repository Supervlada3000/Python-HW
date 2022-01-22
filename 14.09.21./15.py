#Даны два списка с числами, получить третий путем поэлементного сложения первых двух.
a = input().split()
b = input().split()
c = []
for i in range (len(a)):
    s = int(a[i]) + int(b[i])
    c.append(s)
print(c)