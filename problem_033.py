# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

fracs = []

for num in range(10, 100):
    for denom in range(num, 100):
        try:
            curious = int(str(num)[0]) / int(str(denom)[1])
        except ZeroDivisionError:
            continue
        if num / denom == curious:
            fracs.append((num, denom))
