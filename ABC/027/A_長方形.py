##### 解けた #####

import numpy as np

L=np.asarray(list(map(int,input().split(" ")))) # 辺のリスト

# 各辺について見てゆく
for l in L:
    if len(np.where(L==l)[0])%2==1: # 同じ長さが奇数個の場合
        print(l)
        break