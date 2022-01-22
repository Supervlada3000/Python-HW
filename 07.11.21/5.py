#Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO. Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
strok1 = int(input())
stolb1 = int(input())
strok2 = int(input())
stolb2 = int(input())
if strok1%2==0 and strok2%2==0:
    if stolb1%2 == stolb2%2:
        print ('YES')
    else:
        print ('NO')
elif strok1%2!=0 and strok2%2==0:
    if stolb1%2 != stolb2%2:
        print ('YES')
    else:
        print ('NO')
elif strok1%2==0 and strok2%2!=0:
    if stolb1%2 != stolb2%2:
        print ('YES')
    else:
        print ('NO')
elif strok1%2!=0 and strok2%2!=0:
    if stolb1%2 == stolb2%2:
        print ('YES')
    else:
        print ('NO')
