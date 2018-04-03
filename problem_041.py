from itertools import permutations

def is_prime(n: int):
    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def generate_n_pandigitals(n: int):
    initialized_number = ''.join(str(x) for x in range(1, n+1))
    pandigit_numbers = []
    for per in permutations(initialized_number, n):
        pandigit_numbers.append(int(''.join(per)))
    return pandigit_numbers


for x in range(1, 10):
    for pandigit in generate_n_pandigitals(x):
        if is_prime(pandigit):
            print(pandigit)
