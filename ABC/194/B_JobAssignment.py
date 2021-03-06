##### 解けた

N=int(input()) # 従業員の数
J=[[] for _ in range(N)] # 仕事にかかる時間

# リストに格納
for n in range(N):
    A,B=list(map(int,input().split(" ")))
    J[n]=[A,B]

minT=(2e+5)+1 # 最小の時間
T=None # 時間

for i in range(N): # 1人目
    for j in range(N): # 2人目
        if i==j: # 1人目=2人目
            T=J[i][0]+J[j][1] # 時間は合計時間
        else: # 1人目≠2人目
            T=max(J[i][0],J[j][1])

        minT=min(T,minT) # 最小値の更新

print(minT)