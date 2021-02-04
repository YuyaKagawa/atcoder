##### 解けた

r1,c1=list(map(int,input().split(" "))) # 最初の駒
r2,c2=list(map(int,input().split(" "))) # ゴール

b11=c1-r1 # 1の下の切片
b12=c1+r1 # 1の上の切片
b21=c2-r2 # 2の下の切片
b22=c2+r2 # 2の上の切片

flag12=(b11-b22)/2*10%10==0 and (3*b11-b22)/2*10%10==0 # スタートの傾き1とゴールの傾き-1
flag21=(b12-b21)/2*10%10==0 and (3*b12-b21)/2*10%10==0 # スタートの傾き-1とゴールの傾き+1

d11=abs(c1-(r1+b21)) # ゴールの+1の直線と、スタートの距離
d12=abs(c1-(-r1+b22)) # ゴールの-1の直線と、スタートの距離

if (r1==r2) and (c1==c2): # 同じ位置の判定
    print(0)
elif (abs(r1-r2)+abs(c1-c2))<=3: # マンハッタン距離で3以内
    print(1)
elif ((r1+c1)==(r2+c2)) or ((r1-c1)==(r2-c2)): # 斜め方向に1回
    print(1)
elif min(d11,d12)<=4: # 3移動→斜めで2回
    print(2)
elif flag12==True or flag21==True: # 斜め→斜めで2回
    print(2)
elif (abs(r1-r2)+abs(c1-c2))<=6: # マンハッタン距離で6以内
    print(2)
else: # 縦横→斜め→斜めで3回
    print(3)