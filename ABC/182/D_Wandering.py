##### 解けた、解説や他の人の実装を見た、よくわかんない

N=int(input()) # 数列の長さ
A=list(map(int,input().split(" "))) # 数列

# 動作iの合計の座標の変化
S=[0]*(N+1)

for i in range(N): # 要素の作成
    S[i+1]=S[i]+A[i]

print(S)

maxS=0

K=[0]*(N+1) # 累計の動き

maxV=[0]*(N+1)

for i in range(N): # 各動作について
    maxS=max(maxS,S[i+1])
    maxV[i]=K[i]+maxS
    K[i+1]=K[i]+S[i+1] # 累計を計算してゆく

print(max(maxV))

# import numpy as np


# # 動作iの合計の座標の変化
# p=[sum(A[:i+1]) for i in range(N)] 

# # 動作iを座標0で始めたときの、開始から終了までの座標の最大値
# q=[np.cumsum(A[:i+1]).max() for i in range(N)] 

# r=0
# x=0

# for i in range(N):
#     r=max(r,x+q[i])
#     x=x+p[i]

# print(r)


### 以下は自力でやったとき
# s=0 # 合計値
# s_max=0 # 合計値の最大

# for i in range(N): # 各数字について
#     for j in range(i+1): # 各数字について
#         s+=A[j] # 合計に合算
#         s_max=max(s_max,s) # 最大値の更新

# print(s_max)


