okane = 0
count = 1
for opo in range(3):
    for ftp in range(5):
        for twp in range(11):
            for tenp in range(21):
                for fp in range(41):
                    for tp in range(101):
                        okane = 100*opo+50*ftp+20*twp+10*tenp+5*fp+2*tp
                        if okane <= 200:
                            count += 1
                            print(opo,ftp,twp,tenp,fp,tp)
print(count)