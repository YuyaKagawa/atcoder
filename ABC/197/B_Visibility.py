##### 解けた

H,W,X,Y = list(map(int,input().split(" ")))
S=[[] for _ in range(H)]
X-=1
Y-=1

for h in range(H):
    s = list(input())
    S[h]=s

count=1 # カウント、そのマス自身がまずある

# 上方向
for u in range(1,X+1):
    if S[X-u][Y]==".":
        count+=1
    else:
        break

# 下方向
for d in range(1,H-X):
    if S[X+d][Y]==".":
        count+=1
    else:
        break

# 右方向
for r in range(1,W-Y):
    if S[X][Y+r]==".":
        count+=1
    else:
        break

# 左方向
for l in range(1,Y+1):
    if S[X][Y-l]==".":
        count+=1
    else:
        break



print(count)