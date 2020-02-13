### Provide a solution to problem #699
from fractions import Fraction
from utils.factorization import factorMultiplicity

N = 10 ** 14


def _sigma(n: int) -> int:
    """Calculate the sum of the divisors of an integer n"""
    factorization = factorMultiplicity(n)
    sigma = 1
    for p_n in factorization:
        sigma *= (p_n[0] ** (p_n[1] + 1) - 1) / (p_n[0] - 1)
    return int(sigma)


def _is_power_of_three(number: int) -> bool:
    """Determine if a given number is power of three"""
    factorization = factorMultiplicity(number)
    if len(factorization) == 1 and factorization[0][0] == 3:
        return True
    else:
        return False


def T(N: int) -> int:
    """Calculate the function defined by the problem"""
    sum = 0
    for n in range(1, N+1):
        divisor_fraction = Fraction(_sigma(n), n)
        if _is_power_of_three(divisor_fraction.denominator):
            sum += n
    return sum



prior = 0
for x in range(1, 1000):
    new = T(x)
    if new != prior:
        fraction = Fraction(_sigma(x), x)
        print(fraction, new)
        prior = new
