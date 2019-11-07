##### 解けた #####

import numpy as np

N=int(input())
A=np.asarray(list(map(int,input().split(" "))))
count=0

while True:
    if (A%2==1).sum()==0:
        A=A/2
        count+=1
    else:
        break
        
print(count)