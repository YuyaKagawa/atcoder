##### 解けてない #####

# import numpy as np

R,C=list(map(int,input().split(" ")))
sy,sx=list(map(int,input().split(" ")))
gy,gx=list(map(int,input().split(" ")))
sy,sx,gy,gx=sy-1,sx-1,gy-1,gx-1

# L=np.full((R,C),"#",np.str) # 迷路

L=[] # 迷路

# 迷路を読み込んでゆく
for r in range(R):
    # L[r,:]=list(input())
    L.append(list(input()))

# print("迷路")
# print(L)

queue=[[sy,sx]] # 現在の捜索候補、最初はスタート
alist=[] # 既に訪れたノードのリスト
# parent=np.empty((R,C),dtype=object) # 各ノードの親ノードのリスト
parent=[[[] for _ in range(C)] for _ in range(R)] # 各ノードの親ノードのリスト
parent[sy][sx]="s"
Finflag=False # 探索終了のフラグ

# キューの中身がある限り続ける
while len(queue)>0:
    ny,nx=queue.pop(0) # キューの中の最初のノードを取得し、それを現在のノードとする
    # print("now = ",ny,nx)
    # print("alist = ",alist)

    alist.append([ny,nx]) # 訪れたノードのリストに追加

    # 現在のノードの子ノードの候補
    ccand=[[ny-1,nx],[ny,nx+1],[ny+1,nx],[ny,nx-1]] 
    child=[] # 探索上の子ノードのリスト

    # print("子ノードの候補 = ",ccand)

    for c in ccand:
        # print("c = ",c)

        if (c not in alist) and (L[c[0]][c[1]]=="."):
            queue.append(c)
            parent[c[0]][c[1]]=[ny,nx]

            if c==[gy,gx]: # 次がゴールなら終了
                Finflag=True
                break

        if Finflag:
            break

    if Finflag:
        break


# rn=[gy,gx] # これから親ノードのリストを辿って経路を取得する
# path=[[gy,gx]] # 経路のリスト

# while rn!="s":
#     rn=parent[rn[0]][rn[1]] # 親のノードを取得

#     if rn==[sy,sx]: # スタート地点なら終了
#         break

#     path.append(rn)

# print(path)
# print(len(path))