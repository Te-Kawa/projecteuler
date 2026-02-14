wa = set()
for i in range(2,90):
    for n in range(123,6790):
        a = i * n 
        b = str(i) + str(n) + str(a)
        c = set(b)
        if not '0' in c:
            if len(b) == len(c) == 9:
                wa.add(a)
                print(i,n,a)
print(sum(wa))