##### 解けた #####

M,D=list(map(int,input().split(" ")))

if M%D==0: # 月が日で割り切れる場合
    print("YES")
else: # 割り切れない場合
    print("NO")