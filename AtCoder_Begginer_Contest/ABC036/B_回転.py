##### 解けた #####

import numpy as np

N=int(input())
S=np.full((N,N),"x",np.str)

for n in range(N): # 入力
    S[n,:]=list(input())

for s in np.rot90(S,3): # 反時計回りに270°回転させる
    print("".join(s))