from math import sqrt, gcd, floor
import datetime


def sigma(n: int):
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
    sum = 0
    mod = 10**9
    for x in range(1, n+1):
        for y in range(1, n+1):
            if x > 1 and y > 1 and gcd(x, y) == 1:
                sum += (sigma(x)*sigma(y)) % mod
            else:
                sum += sigma(x*y) % mod
            # root = sqrt(x*y)
            # if is_prime(x*y):
            #     add = x*y + 1
            #     sum += add
            # elif root.is_integer():
            #     add = (2**(root+1)) - 1
            #     sum += add
            # else:
            #     add = sigma(x*y)
            #     sum += add
    return int(sum - 1)

cache = {}


def S(N: int):
    if cache.get(N):
        return N
    else:
        overcount = 0
        for i in range(1, N+1):
            overcount += i * floor(N/i)
        correction = 0
        for j in range(2, N+1):
            correction += j * S(floor(N/j))
    answer = overcount ** 2 - correction
    cache.update({N: answer})
    return answer

start_time = datetime.datetime.now()
S(10**11)
end_time = datetime.datetime.now()
print(end_time - start_time)