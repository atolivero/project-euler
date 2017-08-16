sum = 0
for x in [num for num in range(1000) if num % 3 == 0 or num % 5 == 0]:
   sum += x
print(sum)