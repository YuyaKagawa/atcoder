##### 解けた

N,X=list(map(int,input().split(" "))) # クイズの数N、はじめの点X
S=input() # クイズの結果

x=X # これから変化してゆく点

for s in S: # 各結果について
    if s=="x":
        x=max(0,x-1)
    elif s=="o":
        x+=1

print(x)