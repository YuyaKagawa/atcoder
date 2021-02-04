##### 解けた

N=int(input()) # マスの数
A=list(map(int,input().split(" "))) # マス目
count=0 # カウント

for n in range(N): # 各マスについて
    if (n+1)%2==1 and A[n]%2==1: # 条件を満たす場合
        count+=1

print(count)