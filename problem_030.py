# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

power_of_fifths = []

for num in range(2, 1000000):
    digit_sum = 0
    for digit_index in range(len(str(num))):
        digit_sum += int(str(num)[digit_index]) ** 5
    if digit_sum == num:
        power_of_fifths.append(num)

sum_of_all_fifths = 0
for x in power_of_fifths:
    sum_of_all_fifths += x

print(sum_of_all_fifths)