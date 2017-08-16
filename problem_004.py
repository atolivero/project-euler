import math

def is_palindrome(number: int):
   length = len(str(number))
   length = int(length)
   string = str(number)
   if length % 2 == 0:
       half_way = int(length / 2)
       if string[0:half_way-1] == string[half_way::-1]:
           return True
   else:
       length -= 1
       half_way = int(length / 2)
       if string[0:half_way-1] == string[half_way::-1]:
           return True
   return False

palindromes = []

for x in range(100, 1000):
   for y in range(100, 1000):
       product = x * y
       if is_palindrome(product):
           palindromes.append(product)
           print(product)


# XXXXX
# 01234
# length = 5
# halfway = 2
#
# XXXX
# 0123
# length = 4
# halfway = between 1 and 2

