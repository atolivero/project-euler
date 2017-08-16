# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

def sum_of_digits(x: int) -> int:
    string = str(x)
    length = len(string)

    sum = 0
    for x in range(0, length):
        sum += int(string[x])
    return sum

power = 2 ** 1000

print(sum_of_digits(power))