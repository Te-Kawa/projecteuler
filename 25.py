a = 1
b = 1
f = 0
n = 2
while len(str(f)) < 1000:
    f = a + b 
    n += 1
    if a <= b:
        a = f
    else:
        b = f
print(f,n)