##### 解けた #####

N,L=list(map(int,input().split(" ")))
S=[] # 文字列

for _ in range(N): # 入力
    S.append(input())

# アルファベット順に並び替えた後出力
for s in sorted(S):
    print(s,end="")