##### 解けた、なぜか自力のやつだと通らなかった

from itertools import combinations

N=int(input()) # 点の数
L=[tuple(map(int,input().split(" "))) for _ in range(N)]

flag_g=False # フラグ

for comb in combinations(range(N),3): # 各コンビネーションについて
    x10=L[comb[1]][0]-L[comb[0]][0]
    y10=L[comb[1]][1]-L[comb[0]][1]
    x20=L[comb[2]][0]-L[comb[0]][0]
    y20=L[comb[2]][1]-L[comb[0]][1]

    if y20*x10==y10*x20: # 直線一致判定
        flag_g=True
        break # 終了

if flag_g==True: # フラグが立っている場合
    print("Yes")
else: # フラグが立っていない場合
    print("No")


##################################################
# 以下は自力で実装したもの

# L=[0,0]*N # 点のリスト

# for n in range(N):
#     x,y=list(map(int,input().split(" "))) # 点のxy座標
#     L[n]=[x,y] # リストに入れる

    # xdiff=L[comb[1]][0]-L[comb[0]][0] # 2つ目と1つ目のxの差
    # ydiff=L[comb[1]][1]-L[comb[0]][1] # 2つ目と1つ目のyの差
    
    # if xdiff!=0: # y軸に平行ではない場合
    #     a=ydiff/xdiff # 直線の傾き
    #     b=L[comb[0]][1]-a*L[comb[0]][0] # 直線の切片

    #     if (L[comb[2]][1])==(a*L[comb[2]][0]+b): # 3つ目が直線上にある場合
    #         flag_g=True # フラグを立てる
    # else: # y軸に平行の場合
    #     if L[comb[0]][0]==L[comb[1]][0]==L[comb[2]][0]: # すべてのx座標が同じ場合
    #         flag_g=True # フラグを立てる
