#Написать две функции, которые будут переводить из десятичной СС в двоичную и обратно.
#Из 10 в 2
n = int(input())
b = ''
while n>0:
    b = str(n%2)+ b
    n = n//2
print(b)

#Из 2 в 10
n = input()
b = 0
for i in range (len(n)):
    b = b+(int(n[i])*(2**(len(n)-i-1)))
print(b)