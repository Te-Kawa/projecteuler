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