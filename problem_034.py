# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


import math


def factorial_sum(x: int) -> int:
    string = str(x)
    length = len(string)
    sum = 0
    for x in range(length):
        sum += math.factorial(int(string[x]))
    return sum


total_sum = 0
for number in range(3, 1000000):
    if number == factorial_sum(number):
        print(number)
        total_sum += number

print(total_sum)
