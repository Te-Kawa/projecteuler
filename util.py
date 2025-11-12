import math

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