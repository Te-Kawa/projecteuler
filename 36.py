a = 0
for i in range(1,1000001):
    if i == int(str(i)[::-1]):
        b = int(format(i,'b'))
        if b == int(str(b)[::-1]):
            a += i
print(a)