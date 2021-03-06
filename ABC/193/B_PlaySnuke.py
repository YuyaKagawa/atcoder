##### 解けた

N=int(input()) # 店の数
flagB=False # 買えるかどうかのフラグ
Mmin=(1e+9)+7 # 一番安い

for _ in range(N): # 各店について
    A,P,X=list(map(int,input().split(" ")))

    if (X-A)>0: # もし在庫がある場合
        flagB=True # フラグをTrueに
        Mmin=min(Mmin,P) # 最小値の更新

if flagB==False: # もし買えない場合
    print(-1)
else: # もし買える場合
    print(Mmin)