def is_prime(x: int):
   prime = True
   for y in range(2, x):
       if x % y == 0:
           return False
   return prime

primes = [2]
position = 0

while position < 10001:
   for x in range(3,10000000000000):
       if is_prime(x):
           primes.append(x)
           print(str(position) + ' prime is ' + str(x))
           position += 1
