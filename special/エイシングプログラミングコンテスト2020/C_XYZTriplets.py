##### 解けた、解説見た

from math import sqrt

N=int(input()) # 整数
C=[0]*(N+1) # カウントのリスト
l=int(sqrt(N)) # せいぜいこの範囲

for x in range(1,l+1):
    for y in range(1,l+1):
        for z in range(1,l+1):
            s=x**2+y**2+z**2+x*y+y*z+z*x # 合計

            if s<N+1: # もしありえるなら
               C[s]+=1 # カウントをインクリメント

for n in range(1,N+1): # 各値について
    print(C[n])

