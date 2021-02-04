###### 解けた #####

import numpy as np

N,Y=list(map(int,input().split(" ")))
y=Y/1000 # 後の計算を楽に
sol=[] # 通り

for a in range(0,N+1):
    b=(-1/4)*(9*a-y+N)
    c=N-a-b

    # b,cが0以上の整数の場合、解となる
    if b>=0 and b.is_integer() and c>=0 and c.is_integer():
        sol=list(map(str,list(map(int,[a,b,c]))))
        break

if len(sol)==0: # 解が見つからなかった場合
    print("-1 -1 -1")
else: # 解が見つかった場合
    print(" ".join(sol))