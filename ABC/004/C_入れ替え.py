##### 解けた #####

N=int(input())%30 # 30回周期
C=[str(i+1) for i in range(6)] # カード

# 入れ替え作業を繰り返す
for n in range(N):
    ### 入れ替え
    t=C[(n%5)]
    C[(n%5)]=C[(n%5)+1]
    C[(n%5)+1]=t

print("".join(C))