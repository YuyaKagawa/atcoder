##### 解けた

N=int(input()) # 点の数
P=[[] for _ in range(N)] # 点のリスト

def cal_g(p1,p2): # 傾きを計算する関数
    return (p2[1]-p1[1])/(p2[0]-p1[0])

# 入力をリストに格納
for n in range(N):
    P[n]=list(map(int,input().split(" ")))

count=0 # 求める組の数

for i in range(0,N-1): # 各i
    for j in range(i+1,N): # 各j
        g=cal_g(P[i],P[j]) # 傾きを計算

        if -1<=g<=1: # -1以上+1以下の場合
            count+=1 # カウント

print(count)