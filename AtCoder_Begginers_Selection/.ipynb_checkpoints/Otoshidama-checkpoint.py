###### 解けていない #####

import numpy as np

N,Y=list(map(int,input().split(" ")))
K=np.array([10000,5000,1000])
n1k=Y//1000 # 全部1000円札の場合に必要な枚数
n10k=(n1k-N)//9
n5k=(n1k-N-9*n10k)//4
n1k=n1k-10*n10k-5*n5k

if (n10k+n5k+n1k)==N:
    print(n10k,n5k,n1k)
else:
    print("-1 -1 -1")