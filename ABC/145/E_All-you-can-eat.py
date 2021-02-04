##### 解けてない #####

from itertools import permutations

N,T=list(map(int,input().split(" ")))
D=[]

for _ in range(N):
    d=list(map(int,input().split(" ")))
    D.append(d)

maxv=0

for p in list(permutations(D,N)):
    vsum=0
    tsum=0


    for pi in p:
        tsum+=pi[0]

        if tsum<=T-0.5:
            tsum+=pi[1]
        else:
            break

    if maxv<tsum:
        maxv=tsum

print(maxv)        