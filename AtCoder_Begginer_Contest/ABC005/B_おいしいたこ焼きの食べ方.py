##### 解けた #####

N=int(input())
T=[] # たこ焼きのリスト

# 入力をリストに追加してゆく
for _ in range(N):
    T.append(int(input()))

print(min(T))