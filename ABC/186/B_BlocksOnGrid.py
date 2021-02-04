##### 解けた

H,W=list(map(int,input().split(" ")))
B=[] # ブロックの数のリスト
minn=100 # 最小の個数

# 各入力について
for h in range(H):
    row=list(map(int,input().split(" "))) # 1行ずつ
    B.append(row) # リストに追加
    minn=min(minn,min(row)) # 最小値の更新

s=0 # 積み上げる数

# 各ブロックの数について
for h in range(H):
    for w in range(W):
        s+=B[h][w]-minn # 多い分を積み上げてゆく

print(s)