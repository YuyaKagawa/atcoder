##### 解けた #####

L,H=list(map(int,input().split(" ")))
N=int(input())

# 各運動について
for _ in range(N):
    a=int(input())

    if a<L: # 運動が足りない場合
        print(L-a)
    elif H<a: # 運動が適切な場合
        print(-1)
    else: # 運動が過剰ば場合
        print(0)