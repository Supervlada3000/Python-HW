#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
def is_prime():
   if n < 2:
       return False
   if n == 2:
       return True
   i = 2
   while i <= n**(1/2):
       if n % i == 0:
           return False
       i += 1
   return True
n = int(input())
print(is_prime())