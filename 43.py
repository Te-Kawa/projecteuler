
import itertools
a = 0
prime = [2,3,5,7,11,13,17]
for i in itertools.permutations('0123456789'):
    b = ''.join(i)
    for n in range(2,9):
        if not (int(b[n-1])*100 + int(b[n])*10 + int(b[n+1])) % prime[n-2] == 0:
            break
    else:
        print(i)
        a += int(b)
print(a)