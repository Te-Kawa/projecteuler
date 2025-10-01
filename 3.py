n = 600851475143 
p = []
for i in range(2,n):
    
    if n%i == 0:
        p += [i]
        n = n//i
        print(n,i)
        if n==1:
            print(p)
            break
