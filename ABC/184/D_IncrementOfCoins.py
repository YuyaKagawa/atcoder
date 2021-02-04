##### 解けた
##### ヒント見た、他の人のを参考に

A,B,C=list(map(int,input().split(" "))) # コインの枚数
l=[[[0.0 for _ in range(101)] for _ in range(101)] for _ in range(101)] # リスト

# 回数の期待値を取得する関数
def get(A,B,C):
    for i in range(100,-1,-1):
        for j in range(100,-1,-1):
            for k in range(100,-1,-1):
                if max(i,j,k)==100: # i,j,kのどれかが100の場合、0
                    l[i][j][k]=0
                elif i<A or j<B or k<C: # i,j,kのどれかが目的のものよりも小さくなった場合、次の候補へ
                    break
                elif max(i,j,k)<100: # i,j,kのどれも100でない場合
                    s=i+j+k # 合計
                    l[i][j][k]=float(i)/s*(l[i+1][j][k]+1.0)+float(j)/s*(l[i][j+1][k]+1.0)+float(k)/s*(l[i][j][k+1]+1.0) # 計算

                    if i==A and j==B and k==C: # 目標に到達したら終了
                        return l[A][B][C]

    return l[A][B][C] # 0,0,0のときの出力

print(get(A,B,C))