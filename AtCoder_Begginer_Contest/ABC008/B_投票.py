##### 解けた #####

import numpy as np

N=int(input()) # 構成員の数
S=np.full((N,),"a",dtype=object) # 構成員のリスト

# 候補者を見てゆく
for n in range(N):
    S[n]=input()

maxcount=0 # 最大カウント
maxu="" # 最大カウントの構成員

# 各ユニークについて
for u in np.unique(S):
    countu=np.count_nonzero(S==u) # ユニーク数
    
    if countu>maxcount: # ユニーク数が今までの最大カウントよりも大きい場合
        maxcount=countu # 最大を更新
        maxu=u # 構成員を更新

print(maxu)    