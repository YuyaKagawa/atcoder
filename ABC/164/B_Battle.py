##### 解けた

A,B,C,D=list(map(int,input().split(" ")))
w="no one" # 勝者の名前

while A>0 and C>0: # 勝負がつくまで
    C-=B # 高橋の攻撃

    if C<=0: # 相手を倒したら、高橋の勝ち
        w="takahashi"
        break

    A-=D # 青木の勝ち

    if A<=0: # 相手を倒したら、青木の勝ち
        w="aoki"
        break

if w=="takahashi": # 高橋の勝ちの場合
    print("Yes")
else: # 青木の勝ちの場合
    print("No")