import math
n = 0
a = 1
def count_divisor(n):
    count = 0
    i=1
    while i <= n**0.5:
        if n % i == 0:
            count += 2
        if math.sqrt(n).is_integer():
            count -= 1
        i += 1
    return count

while count_divisor(n) < 500:
    print(n,count_divisor(n))
    n += a
    a += 1

print(n)