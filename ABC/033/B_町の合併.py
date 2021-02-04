##### 解けた #####

import numpy as np

N=int(input())
T=np.empty((N,2),dtype=object)

for n in range(N):
    T[n,:]=input().split(" ")

T[:,1]=T[:,1].astype(int) # 人口はint型に変換
to=np.where(T[:,1]>T[:,1].sum()//2)[0] # 人口が合計人口の過半数の町

if len(to)==1: # もし過半数の町があったら
    print(T[to[0],0])
else: # 過半数の町がないなら
    print("atcoder")