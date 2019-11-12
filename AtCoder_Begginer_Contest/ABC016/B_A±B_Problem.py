##### 解けた #####

A,B,C=list(map(int,input().split(" ")))
sumf,subf=False,False # 足し算、引き算であることを示すフラグ

if (A+B)==C: # A+B=Cが成り立つ場合
    sumf=True

if (A-B)==C: # A-B=Cが成り立つ場合
    subf=True

if sumf and subf: # 足し算と引き算の両方の可能性がある場合
    print("?")
elif sumf: # 足し算の可能性がある場合
    print("+")
elif subf: # 引き算の可能性がある場合
    print("-")
else: # どちらの可能性もない場合
    print("!")