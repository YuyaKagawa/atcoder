##### 解けた ######

import numpy as np

n0,X=list(map(int,input().split(" ")))
A=np.asarray(list(map(int,input().split(" "))))
Xb=["0"]*n0 # 2進数表現（逆順）
n=n0 # 後のために

# 2進数表現に変換
while n>0:
    Xb[n-1]=str(X//(2**(n-1)))
    X=X%(2**(n-1))
    n-=1

print(np.dot(A,np.asarray(Xb).astype(int)))