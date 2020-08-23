A=list(map(int,input().split(" ")))

if sum(A)>=22: # 22以上なら
    print("bust")
else: # 22未満なら
    print("win")