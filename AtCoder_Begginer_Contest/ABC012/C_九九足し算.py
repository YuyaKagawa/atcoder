##### 解けた #####

import numpy as np

ns=str(2025-int(input())) # 求める積
M=[] # 九九を格納

# 九九を計算し格納する
for i in range(1,10):
    for j in range(1,10):
        M.append([i,j,i*j])

M=np.asarray(M).astype(str) # 形式を変換

# 各九九について見てゆく
for i in np.where(M[:,2]==ns)[0]:
    print(" x ".join(M[i,:2]))