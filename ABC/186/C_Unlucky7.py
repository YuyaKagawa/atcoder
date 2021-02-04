##### 解けた

N=int(input()) # 数

# 10進法で表した、文字列を返す関数
def num10(N):
    return str(N)

# 8進法で表した、文字列を返す関数
def num8(N):
    n=N # これから割ってゆく数
    r=[] # 答えのリスト

    while n>=8: # 8以上の場合
        a=n%8 # あまり
        n=n//8 # 商

        r.append(str(a))

    r.append(str(n))

    return "".join(r)

num=0 # 最終的に出力する数

for i in range(1,N+1):
    n10=num10(i) # 10進数
    n8=num8(i) # 8進数
    num+=int(("7" not in n10) and ("7" not in n8)) # 条件を満たす場合、インクリメント
    
print(num)