import math

def count_divisor(n):
    '''
    約数の数を返す
    nは約数を求めたい数
    '''
    count = 0
    i=1
    while i <= n**0.5:
        if n % i == 0:
            count += 2
        if math.sqrt(n).is_integer():
            count -= 1
        i += 1
    return count
def sinnoyakusuu(n):
    '''
    真の約数をリストで返してくれる
    nは約数を知りたい数
    '''
    p = [1]
    for i in range(2,n):
        if n%i == 0:
            p += [i]
        if n==1:
            break
    return(p)

def soinsuubunkai(n):
    p = []
    for i in range(2,n):
        if i != 2 and i%2 == 0:
            pass
        if n % i == 0:
            while n% i == 0:
                p += [i]
                n = n // i
        if n == 1:
            break
    return(p)

def recurrig_cycle(n):
    '''
    1 / n の循環節の長さを返す。
    n = 6 の場合 0.16666...なので
    6が循環しているら1を返す 
    循環してなかったら 0 を返す
    '''
    a = 0
    b = 1
    c = []
    while True:
        a,b = divmod(b,n)
        # print(a,b)
        if b in c:
            return (len(c)-c.index(b))
        c.append(b)
        if b == 0:
            return 0
        b *= 10

def Is_prime(n):
    for i in range(2,n):
        if i != 2 and i%2 == 0:
            pass
        if n % i == 0:
            return False
        if i > n**0.5:
            return True