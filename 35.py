from util import Is_prime
count = 1
for i in range(3,1000000):
    s = str(i)
    if '0' not in s and '2' not in s and'4' not in s and'6' not in s and'8' not in s:
        for n in range(len(s)):
            if not Is_prime(int(s)):
                break
            s = s[-1]+s[0:-1]
        else:
            count += 1
            print(i)
print(count)