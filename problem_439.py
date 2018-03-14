from math import sqrt

def sum_divisors(n: int):
    """
    Returns the sum of the divisors of an integer n
    Args:
        n: integer

    Returns:
        the sum of the divisors of n
    """
    sum = 0
    for i in range(2, int((sqrt(n)) + 1)):
        if n % i == 0:
            if (i == (n/i)):
                sum += i
            else:
                sum += (i + n//i)
    return sum + n + 1


def S(n: int):
    values_dict = {}
    for x in range (1, n+1):
        for y in range(1, n+1):
            try:
                values_dict[x*y] += 1
            except KeyError:
                values_dict.update({x*y: 1})
    sum = 0
    for key, value in values_dict.items():
        sum += sum_divisors(key) * value
    return sum - 1
