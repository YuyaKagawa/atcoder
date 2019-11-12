##### 解けた #####

import numpy as np

X=input()
A=np.array(["A","B","C","D","E"])

print(np.where(A==X)[0][0]+1)