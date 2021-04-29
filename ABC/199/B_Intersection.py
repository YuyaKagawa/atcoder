##### 解けた #####

import numpy as np

N=int(input())
A=list(map(int,input().split(" ")))
B=list(map(int,input().split(" ")))
S=[0 for _ in range(1002)] # 数値列、0-1001

### ねもす法？

for i in range(N):
    S[A[i]]+=1 # 始まりの印
    S[B[i]+1]-=1 # 終わりの印

Sc=np.cumsum(S) # 累積和

print(len(np.where(Sc==N)[0]))
