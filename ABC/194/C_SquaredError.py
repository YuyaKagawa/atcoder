import numpy as np

N=int(input())
A=np.asarray(list(map(int,input().split(" "))))
S=0

for i in range(1,N):
    S+=((A[i:]-A[:-i])**2).sum()  

print(S)