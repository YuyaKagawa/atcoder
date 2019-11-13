##### 解けた #####

import numpy as np

N=int(input()) # 円の数
R=np.zeros((N,),int) # 円のリスト

# 円を格納
for ri in range(N):
    R[ri]=int(input())

R=R[np.argsort(-R)] # 降順にソート
Asum=0 # 半径*半径のリスト

# 各円について
for ri in range(len(R)):
    r=R[ri]

    if ri%2==0: # 偶数番目のときは+
        Asum+=r*r
    elif ri%2==1: # 奇数番目のときは-
        Asum-=r*r

print(Asum*np.pi) # 最後に半径*半径*pi