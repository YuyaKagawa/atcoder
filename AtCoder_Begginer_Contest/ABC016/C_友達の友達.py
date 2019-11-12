##### 解けてない #####

import numpy as np

N,M=list(map(int,input().split(" ")))
F=np.full((N,N),0,np.int)

for m in range(M):
    a,b=list(map(int,input().split(" ")))
    F[a-1,b-1]=1
    F[b-1,a-1]=1

print(F)
print(np.dot(F,F.T))
print(np.dot(F[0,:],F.T))