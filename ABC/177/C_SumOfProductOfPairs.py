##### 解けた、解説見た

import numpy as np

N=int(input()) # 整数の数
A=list(map(int,input().split(" ")))
sA=np.cumsum(A)%(1000000000+7) # 累積和
s=0 # 合計値

for i in range(0,N-1):
    si=A[i]*(sA[-1]-sA[i]) # 累積和を利用した和
    s=(s+si)%(1000000000+7) # 足してゆく

print(s)
