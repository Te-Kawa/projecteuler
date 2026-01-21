n = 1
a = 2
sa = 0
b = 0
for i in range(2,1001*1001+1):
    sa += 1
    if sa == a:
        n += i
        b += 1
        sa = 0
        if b == 4:
            b = 0
            a += 2
print(n)