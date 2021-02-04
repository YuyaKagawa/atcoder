##### 解けた #####

HW1=list(map(int,input().split(" ")))
HW2=list(map(int,input().split(" ")))

if (HW1[0] in HW2) or (HW1[1] in HW2): # もし高さを揃えられるなら
    print("YES")
else: # 揃えられない場合
    print("NO")