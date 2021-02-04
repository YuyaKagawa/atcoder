##### 解けた #####

import numpy as np

N=int(input())
M=np.full((N,),0)

for n in range(N):
    M[n]=int(input())

count=0
    
while True:
    if len(M)==0:
        break
    else:
        M-=M.min()
        M=M[M>0]
        count+=1
        
print(count)