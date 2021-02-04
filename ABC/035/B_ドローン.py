S=list(input()) # 命令
T=int(input()) # 答えのモード
x,y=0,0 # x,yの位置
c=0 # ?の数

for s in S: # 各命令について
    x,y=x-int(s=="L")+int(s=="R"),y-int(s=="D")+int(s=="U") # 位置を更新
    c=c+int(s=="?") # ?の場合はカウントをインクリメント

if T==1: # 最大値の場合は、最後に?の数を足すだけ
    print(abs(x)+abs(y)+c)
else: # 最小値の場合は、最後に?の数を引くが、引きすぎて逆方向に行きすぎないように
    if c<=(abs(x)+abs(y)): # ?が少ないときは引くだけ
        print(abs(x)+abs(y)-c)
    else: # ?が多いときは、0か1を偶奇で場合分け
        print(int((c-abs(x)+abs(y))%2==1))