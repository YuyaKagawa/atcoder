##### 解けた

Sx,Sy,Gx,Gy=list(map(int,input().split(" ")))

if Gx==Sx: # 同じx座標の場合、除算の都合上場合分け
    print(Sx) 
else:
    xd=float(Gx-Sx) # x座標の差
    yd=float(-Gy-Sy) # y座標の差
    a=yd/xd # 傾き
    b=Sy-a*Sx # 切片
    x=-b/a # y軸との好転

    print(x)