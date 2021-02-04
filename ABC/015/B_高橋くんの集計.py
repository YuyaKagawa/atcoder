##### 解けた #####

import numpy as np
import math 

N=int(input())
A=np.asarray(list(map(int,input().split(" ")))) # ソフトのリスト

print(math.ceil(A[A>0].mean()))