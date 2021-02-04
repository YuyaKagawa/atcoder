##### 解けた

from math import floor,ceil

L,R,d=list(map(int,input().split(" ")))

print(floor(R/d)-ceil(L/d)+1)
