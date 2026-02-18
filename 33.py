d= 1
for a in range(1,9):
    for b in range(a+1,10):
        for c in range(1,10):
            if a/b == ((10*a)+c)/((10*c)+b):
                d *= b/a
                print(((10*a)+c),((10*c)+b))
print(d)
