# №4. дано трехзначное число. Замените среднюю цифру на ноль.
a = int(input())
a1 = a // 100
a3 = a % 10
a = str(a1) + '0' +str(a3)
print (a)