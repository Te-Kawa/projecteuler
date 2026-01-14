from util import recurrig_cycle
a  = []
for i in range(1,1001):
    a.append(recurrig_cycle(i))
print(a.index(max(a))+1)