##### 解けた #####

N,Q=list(map(int,input().split(" ")))
A=[0]*N # 数列

# 各入力に大して、数列を置き換える
for _ in range(Q):
    L,R,T=list(map(int,input().split(" ")))

    # 数列を置き換える
    for i in range(L-1,R):
        A[i]=T

# 出力
for a in A:
    print(a)