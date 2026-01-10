from util import sinnoyakusuu
op = []
aop = set()
for i in range(1,28124):
    if i < sum(sinnoyakusuu(i)):
        op += [i]
for i in range(len(op)):
    for n in range(len(op)):
        if op[i]+op[n] < 28124:
            aop.add(op[i] + op[n])
print (sum(range(28124))-sum(aop))