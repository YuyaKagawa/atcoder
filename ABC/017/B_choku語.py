##### 解けた #####

X=input()
NGflag=False # あり得ないことを示すフラグ

while len(X)>0: # 文字列を全て消化するまで
    if X[0] in ["o","k","u"]: # 最初の一文字が特定の文字の場合
        X=X[1:]
        continue
    elif len(X)>=2: # 長さが2以上の場合
        if X[:2]=="ch": # 最初の二文字が特定の文字の場合
            X=X[2:]
            continue
    
    NGflag=True
    break
    
if NGflag: # choku語ではない場合
    print("NO")
else: # choku語の場合
    print("YES")