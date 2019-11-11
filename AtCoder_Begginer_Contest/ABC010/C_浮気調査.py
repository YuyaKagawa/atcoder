##### 解けた #####

txa,tya,txb,tyb,T,V=list(map(int,input().split(" ")))
n=int(input()) # 女の子の数
d=T*V # あり得る距離
uflag=False # 浮気をしている可能性があることを示すフラグ

# 各女の子について確認してゆく
for _ in range(n):
    x,y=list(map(int,input().split(" "))) # 女の子の居場所
    d1=((x-txa)**2+(y-tya)**2)**(1/2) # スタート→女の子
    d2=((txb-x)**2+(tyb-y)**2)**(1/2) # 女の子→ゴール

    if (d1+d2)<=d: # 可能ならフラグを立てて終了
        uflag=True
        break

if uflag: # 立ち寄り可能なら
    print("YES")
else: # 立ち寄り不可能なら
    print("NO")