##### 解けた、解説見た

N=int(input())
A=list(map(int,input().split(" ")))
s=0

A=sorted(A)
sA=sum(A)

for i in range(N-1):
    sA-=A[i]
    s+=sA-(N-1-i)*A[i]

print(s)