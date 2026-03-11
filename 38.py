a = []
for i in range(1,10000):
    b = ''
    for n in range(1,10):
        b += str(i*n)
        c = set(b)
        if len(b) == len(c) == 9 and  '0' not in b:
            a += [int(b)]
            print(i,n)
            break
        if len(b) >= 10:
            break
print(max(a))
