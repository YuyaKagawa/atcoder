##### 解けた

N=int(input())
A=list(map(int,input().split(" ")))
num_max=0 # カウントの最大値
num_max_k=-1 # 最大のもののk

for k in range(2,max(A)+1):
    num=0 # 割り切れるものの数

    for n in range(N): # 各数字について
        num+=int(A[n]%k==0) # 割り切れる場合、カウントをインクリメント

    if num>=num_max: # 最大値を上回る場合
        num_max=num # 最大値を更新
        num_max_k=k  # kを保持

print(num_max_k)