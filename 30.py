m = []
for i in range(2,(9**5)*7):
    n = i
    a = 0
    for j in str(n):
        a += int(j)**5
    if a == i :
        m += [i]
        print(i)
print(sum(m))