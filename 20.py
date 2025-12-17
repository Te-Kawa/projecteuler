def kaijou(n):
    a = 1
    for i in range(1,n):
        a *= i
    return(a)
n = str(kaijou(100))
a = 0
for i in n:
    a += int(i)
print(a)