from math import factorial
a = 0
for i in range(3,factorial(9)*7):
    b = 0
    for n in str(i):
        b += factorial(int(n))
    if i == b:
        a += i
        print(i)
print(a)