##### 解けた

import math

N=int(input()) # 整数の和
count=0

for a in range(1,N):
    b=math.floor((N-1)/a)
    count+=b
    
print(count)
