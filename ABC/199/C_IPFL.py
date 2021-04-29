N=int(input()) # 文字列の長さの半分
S=input() # 文字列
Q=int(input()) # クエリの数

Si=list(range(len(S))) # 文字列のインデックス

for _ in range(Q): # 各クエリについて
    T,A,B=list(map(int,input().split(" "))) # モード、何文字かの情報

    if T==1: # T=1のとき、A文字目とB文字目を入れ替える
        # S=S[:A-1]+S[B-1]+S[A:B-1]+S[A-1]+S[B:]
        tmp=Si[A-1]
        Si[A-1]=Si[B-1]
        Si[B-1]=tmp
    elif T==2: # T=2のとき、文字列の前半と後半を入れ替える
        # S=S[N:]+S[:N]
        Si=Si[N:]+Si[:N]
    
### 最後に表示
for si in Si:
    print(S[si],end="")

print()
