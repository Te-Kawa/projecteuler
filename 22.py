import urllib.request
with urllib.request.urlopen('https://projecteuler.net/resources/documents/0022_names.txt') as response:
    txt = response.read().decode().replace('"','').split(',')
    txt.sort()
a = 0
for i in range(len(txt)):
    b = 0
    for n in txt[i]:
        b += ord(n)-64
    print(a,i,b)
    a += (i+1) * b
print(a)