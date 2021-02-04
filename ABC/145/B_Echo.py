##### 解けた #####

N=int(input())
S=input()

if N%2==0: # もし文字列の長さが偶数の場合
    if S[:N//2]==S[N//2:]: # もし前半==後半の場合
        print("Yes")
    else: # 前半!=後半の場合
        print("No")
else: # 奇数の場合
    print("No")
