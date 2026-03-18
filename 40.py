a = ''
for i in range(250000):
    a += f'{i}'
print(len(a))
b = int(a[1])*int(a[10])*int(a[100])*int(a[1000])*int(a[10000])*int(a[100000])*int(a[1000000])
print(b)