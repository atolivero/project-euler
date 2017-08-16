# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def find_permutation(x: int) -> int:
    list = []
    for y in range(0, len(str(x))):
        list.append(str(x)[y])
    return set(list)


for x in range(1, 1000000):
    test = find_permutation(x)
    if test == find_permutation(2*x) and test == find_permutation(3*x) and test == find_permutation(4*x) and test == find_permutation(5*x) and test == find_permutation(6*x):
        print(x)
        break