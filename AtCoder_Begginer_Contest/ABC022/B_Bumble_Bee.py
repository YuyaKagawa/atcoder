import numpy as np

N=int(input())
A=np.full((N,),0,np.int) # 花のリスト

# 花をリストに格納してゆく
for n in range(N):
    A[n]=int(input())

C=np.bincount(A)[1:] # 0, 1, 2, 3, ... の個数をカウントしている、0はいらないので省く
C=C[C>0] # 1以上の部分を抜き出す

# 1以上の合計-1以上の長さ
print(C.sum()-len(C))