a = 0
b = 0
c = 0
mfs = 0
pd = 1
def count(y,m):
    global pd,mfs
    if m == 9 or m== 4 or m == 6 or m == 11:
        pd += 30
    elif m == 2:
        if y % 4 == 0 and not(y % 100 == 0 and not y % 400 == 0):
            pd += 29
        else:
            pd += 28
    else:
        pd += 31
    if pd % 7 == 0 and y > 1900:
        # print(i,n,pd)
        mfs += 1
def keisan(y,m):
    global a , b , c , mfs , pd
    for i in range(1900,y):
        for n in range(1,13):
            count(i,n)
            # if n == 9 or n== 4 or n == 6 or n == 11:
            #     pd += 30
            # elif n == 2:
            #     if i % 4 == 0 and not(i % 100 == 0 and not i % 400 == 0):
            #         pd += 29
            #     else:
            #         pd += 28
            # else:
            #     pd += 31
            # if pd % 7 == 0 and i > 1900:
            #     print(i,n,pd)
            #     mfs += 1
    for n in range(1,m+1) :
        count(y,n)
        # if n == 9 or n== 4 or n == 6 or n == 11:
        #     pd += 30
        # elif n == 2:
        #     if y % 4 == 0 and not(y % 100 == 0 and not y % 400 == 0):
        #         pd += 29
        #     else:
        #         pd += 28
        # else:
        #     pd += 31
        # if pd % 7 == 0:
        #     mfs += 1
        #     print(y,n,pd)
    return mfs
print(keisan(2000,12))