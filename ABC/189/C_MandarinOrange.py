##### PyPy3にしたら通った（怒）
N=int(input()) # 皿の数
A=list(map(int,input().split(" "))) # みかんの数
maxv=0 # 最大値

for i in range(0,N):
    MIN=float("inf")

    for j in range(i,N):
        MIN=min(MIN,A[i],A[j])
        v=MIN*(j-i+1)
        maxv=max(maxv,v)

print(maxv)