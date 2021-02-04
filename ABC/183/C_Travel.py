##### 解けた

from itertools import permutations

N,K=list(map(int,input().split(" ")))
T=[] # 入力を受ける配列

# 入力
for n in range(N):
    T.append(list(map(int,input().split(" "))))

P=set(permutations(range(1,N),N-1)) # 順列

num=0 # 合計値がKであるものの数

for p in set(P):
    s=T[0][p[0]] # 合計値

    for i in range(len(p)-1): # 各ノードについて
        s+=T[p[i]][p[i+1]]

    s+=T[p[-1]][0] # 合計値に加算

    if s==K: # もし目標と一致したら
        num+=1 # 数をインクリメント

print(num)