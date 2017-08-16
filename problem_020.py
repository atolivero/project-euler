# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import math

def sum_of_digits(x: int) -> int:
    string = str(x)
    length = len(string)

    sum = 0
    for x in range(0, length):
        sum += int(string[x])
    return sum

one_huned_fac = math.factorial(100)

print(sum_of_digits(one_huned_fac))