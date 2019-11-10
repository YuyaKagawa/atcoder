##### 解けた #####

Ns=input() # string
N=int(Ns) # int

# もし3が含まれるもしくは3で割り切れる場合
if "3" in Ns or N%3==0:
    print("YES")
else:
    print("NO")