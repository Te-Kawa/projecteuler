n=0
for i in range(1000) :
    if i%3 == 0:
        n += i
    elif i%5 == 0:
        n += i

print(n)