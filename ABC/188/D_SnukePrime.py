##### 解説見た

N,C=list(map(int,input().split(" ")))
event=[] # イベントのリスト

# イベントをリストに追加してゆく
for _ in range(N):
    a,b,c=list(map(int,input().split(" "))) 
    event.append([a-1,c])
    event.append([b,-c])

event.sort() # 時刻でソートする
ans=0 # 最終的に出力する値
fee=0 # 単価
t=0 # 今の時刻

for x,y in event:
    if x!=t: # もし時刻が異なっていたら、それまでの分を加算する
        ans+=min(fee,C)*(x-t)
        t=x # 時刻を更新する

    fee+=y # 単価の更新

print(ans)



























s=0
S=set() # 

for n in range(N):
    a,b,c=list(map(int,input().split(" ")))
    # Labc[n]=[a,b,c]

    

    s+=min(c,C)*(b-a+1)

print(s)



###################################

import numpy as np

N,C=list(map(int,input().split(" ")))
m=0
Labc=[[] for _ in range(N)]

for n in range(N):
    a,b,c=list(map(int,input().split(" ")))
    Labc[n]=[a,b,c]
    m=max(a,b,m)

L=[0]*(m+1) # リスト

for n in range(N):
    a,b,c=Labc[n]
    L[a-1]+=c
    L[b]-=c

Lcs=np.cumsum(L)

for i in range(0,m+1):
    Lcs[i]=min(Lcs[i],C)


print(sum(Lcs[:]))


##############################
# L=np.zeros(1000000000) # リスト

# print(m)

    # print(input().split(" "))

    # print(list(map(int,input().split(" "))))

    # abc=list(map(int,input().split(" ")))
    # a,b,c=abc[0],abc[1],abc[2]
    # a,b,c=list(map(int,input().split(" ")))




# print("before cumsum  = ",Lcs)
# print("before = ",L)


# print("after cumsum = ",Lcs)
