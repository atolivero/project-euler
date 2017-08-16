sum_of_squares = 0
sum = 0

for x in range(1, 101):
   sum += x
   sum_of_squares += x ** 2
print(sum_of_squares)

square_of_sum = sum ** 2
print(square_of_sum)

diff = square_of_sum - sum_of_squares

print(diff)
