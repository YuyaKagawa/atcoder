##### 解けた、ヒント見た

import numpy as np

# N: 人数、W: 毎分出る水のリットル
N,W=list(map(int,input().split(" ")))

U=[0]*(2*100000+1) # お湯の使用量

# いもす法
for _ in range(N):
    s,t,p=list(map(int,input().split(" ")))

    U[s]+=p # 最初にプラス
    U[t]-=p # 最後にマイナス

if np.cumsum(U).max()<=W: # 累積和を取る
    print("Yes")
else:
    print("No")