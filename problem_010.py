# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import csv
from pathlib import Path

def is_prime(x: int):
   prime = True
   for y in range(2, x):
       if x % y == 0:
           return False
   return prime

prime_list = []

for x in range(2, 3000000):
    if is_prime(x):
        prime_list.append(x)
        print(x)
    if x > 2000000:
        break

sum_of_primes = 0
for x in prime_list:
    sum_of_primes += x

print(sum_of_primes)

file = Path("/Users/alexanderolivero/PycharmProjects/ProjectEuler/Problem_Files/" + "primes_less_than_2_mil.csv")
file.touch()

with file.open('w') as outfile:
    prime_writer = csv.writer(outfile, delimiter=',')
    prime_writer.writerow(prime_list)


