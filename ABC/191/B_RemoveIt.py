##### 解けた

import re

N,X=input().split(" ")
N=int(N)
A="r"+"rr".join(input().split(" "))+"r"
reg=re.compile(r"r%sr"%X)
Ar=re.sub(reg," ",A)
Ar=Ar.replace("r"," ")
Ar=re.sub("[\s]+"," ",Ar)

if len(Ar)>=1 and Ar[0]==" ":
    Ar=Ar[1:]

if len(Ar)>=1 and Ar[-1]==" ":
    Ar=Ar[:-1]

print(Ar)


