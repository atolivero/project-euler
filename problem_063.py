# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

n_digit_count_list = []
for num_length in range(1, 6):
    print(int(str(1)+str(0)*(num_length-1)), int(str(9)*num_length)+1)
    for num in range(int(str(1)+str(0)*(num_length-1)), int(str(9)*num_length)+1):
        for test_pow in range(1, int(num/2) + 1):
            if test_pow ** num_length == num:
                n_digit_count_list.append((num_length, num))
sd