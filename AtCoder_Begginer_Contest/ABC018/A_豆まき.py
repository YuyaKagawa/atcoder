import numpy as np

A=int(input())
B=int(input())
C=int(input())
S=100-np.array([A,B,C]) # 逆順にするために
Ssort=S[np.argsort(S)] # 降順にソート

# 降順にソートした順番を示す
for s in S:
    print(np.where(Ssort==s)[0][0]+1)