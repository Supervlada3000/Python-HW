#Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
d = {}
n = int(input())
for i in range (n):
    l = input().split()
    for j in l:
        d[j] = d.get(j, 0) + 1
mx = max(d.values())
for k, v in d.items():
    if v == mx:
        print(k)