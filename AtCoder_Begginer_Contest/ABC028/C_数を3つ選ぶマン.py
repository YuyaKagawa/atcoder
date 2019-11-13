##### 解けた #####

from itertools import combinations
import numpy as np

N=list(map(int,input().split(" ")))
comb=list(combinations(N,3)) # コンビネーションのリスト
S=np.zeros((len(comb),),int) # 合計のリストに追加

# 各コンビネーションについて合計を計算
for ci in range(len(comb)):
    S[ci]=sum(comb[ci]) # リストに追加

print(np.sort(S)[-3])