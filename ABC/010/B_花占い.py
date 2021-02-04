##### 解けた #####

n=int(input()) # 花の数
A=list(map(int,input().split(" "))) # 花弁の数
C=[] # 何枚減らすかのリスト

# 各花について
for a in A:
    count=0 # 1ずつ減らしてゆく
    ac=a # これが減らした結果

    # 条件を満たすまで減らしてゆく
    while True:
        if ac%2==0 or ac%3==2: # 満たしていない場合
            count+=1 # 1減らす
            ac=a-count # 更新
        else: # 満たす場合、終了
            break

    C.append(count) # リストに追加

print(sum(C))