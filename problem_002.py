fib_nums = [1,2]
pos = 2
while True:
   fib_nums.append(fib_nums[pos-2] + fib_nums[pos-1])
   if fib_nums[pos] > 4000000:
       break
   pos += 1
sum = 0
for num in fib_nums:
   if num % 2 == 0:
       sum += num