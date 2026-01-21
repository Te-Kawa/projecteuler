from util import Is_prime
an,aa,ab =0,0,0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0
        while True:
            if Is_prime(n**2 + a*n + b):
                n += 1
            else:
                if an < n :
                    aa,ab,an = a,b,n
                    print(a,b,n)
                break
print(aa,ab,an  , aa*ab)

