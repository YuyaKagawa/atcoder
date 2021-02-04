##### 解けた

import heapq

N=int(input())
S=[] # 優先度付きヒープ
d=0 # 最終的に埋めたい差

for n in range(N):
    a,b=list(map(int,input().split(" ")))
    d+=a # 埋めるべき（青木派-高橋派）の差
    heapq.heappush(S,-(2*a+b))
    
count=0 # 何個かのカウント

while d>=0:
    s=-(heapq.heappop(S)) # 最も大きいもの
    d-=s # 差を埋める
    count+=1 # カウントをインクリメント

print(count) # カウントを表示