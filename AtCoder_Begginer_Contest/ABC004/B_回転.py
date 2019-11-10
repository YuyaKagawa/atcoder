##### 解けた #####

import numpy as np

B=np.full((4,4),".",dtype=np.str) # 出力する盤面

# 入力を逆順になるように盤面に入れていく
for i in range(4):
    B[i,:]=input().split(" ")

# 180度回転させたものを1行ずつ出力してゆく
for r in np.rot90(B,2):
    print(" ".join(r))