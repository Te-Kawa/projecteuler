n = 0
a = 1
b = 1
f = 1
while n < 100000000 :
    f = a + b 
    if f % 2 == 0:
        n += f

    if a <= b:
        a = f
    else:
        b = f

print(n)