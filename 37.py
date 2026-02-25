from util import Is_prime
a = 0
for i in range(10,1000001):
    if Is_prime(i):
        p = str(i)
        for n in range(1,len(str(i))):
            if not Is_prime(int(p[n:])):
                break
            if not Is_prime(int(p[:-n])):
                break
        else:
            a += i
            print(i)
print(a)