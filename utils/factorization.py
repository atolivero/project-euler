

def factor(n, startFrom=2):
    """returns a list of prime factors of n,
    knowing min possible >= startFrom."""
    if n <= 1:  return [ ]
    d = startFrom
    factors = [ ]
    while n >= d*d:
      if n % d == 0:
        factors.append(d)
        n = n/d
      else:
        d += 1 + d % 2  # 2 -> 3, odd -> odd + 2
    factors.append(n)
    return factors


def countConsecutiveSame(seq):
    '''Given a sequence, return a list of (item, consecutive_repetitions).'''
    if not seq: return []
    current = NotImplemented
    n = 0
    pairs = []
    for e in seq:
        if e == current:
            n += 1
        else:
            if n > 0:
                pairs.append((current, n))
            n = 1
            current = e
    pairs.append((current, n))
    return pairs


def factorMultiplicity(n):
    return countConsecutiveSame(factor(n))


def listPrimes(n):
    '''Return a list of all primes < n using the Sieve of Eratosthenes.'''
    if n <= 2:  return []
    sieve = [True]*n # indices 0 ... n-1, ignore 1 and even.  Entries at odd
        #  indices greater than 2 will be changed to false when found not prime
    primes = [2]
    i = 3
    while(i < n):
        if sieve[i]:  # First number not eliminated must be prime
            primes.append(i)      # next eliminate multiples of i:
            for mult in range(i*i, n, i): # Note multiples with a smaller
                sieve[mult] = False       #   factor are already eliminated
        i += 2  # skip even numbers
    return primes
