##### 解けた #####

N,S,T=list(map(int,input().split(" ")))
W=int(input())
count=int((W>=S) and (W<=T)) # カウント

for _ in range(N-1):
    a=int(input()) # 体重の変化量
    W=W+a # 変化する

    if W>=S and W<=T: # ベストボディーの場合
        count+=1 # カウントを増加

print(count)