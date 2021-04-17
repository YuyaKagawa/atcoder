##### 解けた

N,M=list(map(int,input().split(" ")))

A=list(map(int,input().split(" "))) # 数列A
B=list(map(int,input().split(" "))) # 数列B

sA=set(A) # 数列Aをset型で
sB=set(B) # 数列Bをset型で
U=set() # ユニークな数の集合

for a in sA: # 数列Aの数字を1個ずつ
    if not a in sB: # 数列Bに含まれない場合
        U.add(a) # 新たな集合に追加
    
for b in sB: # 数列Bの数字を1個ずつ
    if not b in sA: # 数列Aに含まれない場合
        U.add(b) # 新たな集合に追加

print(" ".join(list(map(str,sorted(list(U),reverse=False)))))

