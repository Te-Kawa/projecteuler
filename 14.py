i = 1
c = 0
a = 0
ac = 0
while i <= 1000000:
    n = i
    while n != 1:        
        if n % 2 == 0:
            n = n/2
            c += 1
        else:
            n = 3*n+1
            c += 1
    print(a, c)
    if ac < c:
        a = i
        ac = c
        print(a,ac)
    i += 1
    c = 0
print(a,ac)