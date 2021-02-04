##### 解けた #####

import numpy as np
from itertools import combinations

N,M=list(map(int,input().split(" "))) # N人、M個の関係性
R=np.zeros((N,N),dtype=np.int) # 関係性隣接行列

# 各関係について、隣接行列を1にしてゆく
for _ in range(M):
    x,y=list(map(int,input().split(" ")))
    R[x-1,y-1]=1
    R[y-1,x-1]=1
    
nlist=np.arange(N) # 今後のための番号のリスト
maxc=1 # 最大クリークの大きさ1
okflag=False # 終了のためのフラグ

### 方策: メンバーのcombinationを見て該当する行列を抜き出し、それが全ての辺で1であるかを見る
# 大きい方から見てゆく
# 辺の数は合計値で判定
for num in reversed(range(1,min(M+2,N+1))):
    sumr=num*(num-1) # 全結合の場合の合計値

    for c in combinations(nlist,num): # 各コンビネーションについて
        if R[list(c),:][:,list(c)].sum()==sumr: # もし全辺が存在するなら
            maxc=num # 求める最大値を更新
            okflag=True # 終了のためのフラグを立てる
            break

    if okflag: # フラグが立っているなら終了
        break

print(maxc)