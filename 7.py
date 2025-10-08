i = 3
p = [2]
while len(p)<10001:
    is_prime = True
    for n in p:
        if i % n == 0:
            is_prime = False
    if is_prime:
        p += [i]
    i += 1
print(p[-1])

