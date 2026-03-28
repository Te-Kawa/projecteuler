import urllib.request
with urllib.request.urlopen('https://projecteuler.net/project/resources/p042_words.txt') as response:
    txt = response.read().decode().replace('"','').split(',')
    txt.sort()
a = 0
tri = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378]
#tri2 = [n*(n+1)//2 for n in range(1,28)]
for i in range(len(txt)):
    b = 0
    for n in txt[i]:
        b += ord(n)-64
    if b in tri:
        a += 1
print(a)