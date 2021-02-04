##### 解けた #####

N=int(input())
Q=[0 for _ in range(4)] # 8, 4, 2, 1の商
Q[0]=(N//8)
Q[1]=((N%8)//4)
Q[2]=(((N%8)%4)//2)
Q[3]=((N%8)%4)%2

print(sum(Q)) # 整数の個数

# 整数を表示
for i in range(len(Q)):
    q=Q[3-i]

    if q>0: # 1以上の場合のみ表示
        print(q*(2**i))