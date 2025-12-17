from util import sinnoyakusuu
a = 0
for n in range(1,10000):
    b = sum(sinnoyakusuu(n))
    print(n, b)
    if b != 1:
        if n == sum(sinnoyakusuu(b)) and n != b:
            a += n
            print(a,n)
print(a)