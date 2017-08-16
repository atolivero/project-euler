import math

def is_prime(x: int):
   prime = True
   for y in range(2, x):
       if x % y == 0:
           return False
   return prime

num = 600851475143
prime_factors = []
floor = math.floor(num / 2)

for x in range(1, floor):
   if num % x == 0 and is_prime(x):
       prime_factors.append(x)
       print(str(x) + ' is a prime factor')

print('done')