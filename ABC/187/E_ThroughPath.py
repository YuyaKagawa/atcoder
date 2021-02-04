
N=int(input()) # 頂点の数
P=[[[] for _ in range(N)] for _ in range(N)]
C=[[] for _ in range(N)] # 値

for _ in range(N-1): # 各編について
    a,b=list(map(int,input().split(" ")))

    print("a,b = ",a,b)

    P[min(a-1,b-1)][max(a-1,b-1)]=[min(a-1,b-1),max(a-1,b-1)]
    # P[b-1][a-1]=[b-1,a-1]

    
for i in range(0,N-1): # 各スタート地点について
    for j in range(i+1,N): # 各ゴール地点について
        # if i==j: # スタート==ゴールの場合、次へ
        #     continue
        # else:
        print(i,j,P[i][j])


