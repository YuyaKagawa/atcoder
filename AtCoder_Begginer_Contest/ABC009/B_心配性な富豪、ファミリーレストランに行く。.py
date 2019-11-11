##### 解けた #####

import numpy as np

N=int(input()) # 料理の数
A=[] # 料理のリスト

# 料理のリストに追加してゆく
for _ in range(N):
    A.append(int(input()))

print(sorted(np.unique(A))[-2])