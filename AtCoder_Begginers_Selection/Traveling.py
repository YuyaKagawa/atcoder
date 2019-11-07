##### 解けた #####

N=int(input()) # 行程の数
NGflag=False # あり得ない行程が含まれているかのフラグ

for _ in range(N):
    t,x,y=list(map(int,input().split(" ")))

    if t<(x+y) or (t-(x+y))%2!=0: # 各行程がありえない場合
        NGflag=True
        break

if NGflag: # あり得ない行程がある場合
    print("No")
else: # 全てありうる場合
    print("Yes")