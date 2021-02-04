##### 解けた #####

import numpy as np

##### いもす法 #####

n=int(input()) # アンケートの数
C=np.zeros((1000001,),np.int) # 色のリスト

# 各アンケートについて、加算してゆく
for _ in range(n):
    a,b=list(map(int,input().split(" ")))
    C[a]+=1 # 下限に+1を足す

    if b<len(C)-1: # 上限+1に-1を足す
        C[b+1]+=-1

# 最後に累積和を取る
print(np.cumsum(C).max())