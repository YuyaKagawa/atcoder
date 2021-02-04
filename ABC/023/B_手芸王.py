##### 解けた #####

N=int(input())
S=input()

if N%2==0: # 偶数の場合あり得ない
    print("-1")
else: # 奇数の場合は考える
    Sl=list(S[:(N-1)//2][::-1]) # 左側、逆順
    Sr=list(S[(N+1)//2:]) # 右側
    NGflag=False

    # 右と左の文字列について
    for i in range(1,N//2):
        sl=Sl.pop(0) # 左の端を取る
        sr=Sr.pop(0) # 右の端を取る
        
        if i%3==0: # 3nのとき
            if sl!="b" or sr!="b":
                NGflag=True
                break
        elif i%3==1: # 3n+1のとき
            if sl!="a" or sr!="c":
                NGflag=True
                break
        elif i%3==2: # 3n+2のとき
            if sl!="c" or sr!="a":
                NGflag=True
                break
        
    if NGflag: # 完成できない場合
        print("-1")
    else: # 完成できる場合
        print(N//2)