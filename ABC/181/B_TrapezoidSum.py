##### 解けた

N=int(input())
s=0 # 合計値

for _ in range(N):
    A,B=list(map(int,input().split(" ")))
    n=B-A+1 # 数
    s+=n*A+int((n-1)*n/2) # 合計

print(s)