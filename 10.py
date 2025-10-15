i = 3
p = [2]
while p[-1]<2000000:
    is_prime = True
    for n in p:
        if n > i**0.5:
            break
        if i % n == 0:
            is_prime = False
    if is_prime:
        p += [i]
    i += 2
    print(len(p), i)
print(sum(p[:-1]))
