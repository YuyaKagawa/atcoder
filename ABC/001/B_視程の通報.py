##### 解けた #####

m=float(input())

if m<100:
    print("00")
elif m<=5000:
    print("{:02.0f}".format(m*10/1000))
elif m<=30000:
    print(int(m/1000+50))
elif m<=70000:
    print(int((m/1000-30)/5+80))
else:
    print("89")