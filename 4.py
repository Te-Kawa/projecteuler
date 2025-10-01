s = 0
n = []
for a in range(100,1000):
    for b in range(100,1000):
        s = str(a*b)
        if s[::-1] == s:
            n += [int(s)]
print(n)