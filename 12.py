# import util
from util import count_divisor

n = 0
a = 1

while count_divisor(n) < 500:
    print(n, count_divisor(n))
    n += a
    a += 1

print(n)