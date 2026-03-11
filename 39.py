a,an = 0,0
for i in range(12,1001):
    bn = 0
    for k in range(1,i-1):
        for l in range(k,i-1):
            m = i-k-l
            if k**2 + l**2 == m**2:
                bn += 1
    if an < bn:
        a,an = i,bn
        print(a,an)
print(a)