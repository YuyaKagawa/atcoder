##### 解けた #####

from itertools import permutations
import math

N=int(input())
T=[] # 町のリスト
lenlist=[] # 距離のリスト

for _ in range(N): # 各町について
    t=list(map(int,input().split(" ")))
    T.append(t)

# 各順列について
for p in list(permutations(T,N)):
    lsum=0

    # 各町について、前後の距離を求める
    for pxi in range(1,len(p)):
        l=math.sqrt((p[pxi][0]-p[pxi-1][0])**2+(p[pxi][1]-p[pxi-1][1])**2)
        lsum+=l

    lenlist.append(lsum)

print(sum(lenlist)/len(lenlist))