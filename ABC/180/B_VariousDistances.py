##### 解けた

from math import sqrt

N=int(input())
X=list(map(float,input().split(" ")))

def distance(X,mode):
    """
    距離を算出する関数
    引数modeで算出方法を指定
    """

    s=0 # 合計値
    
    if mode=="manhattan": # マンハッタン距離
        for x in X:
            s+=abs(x)
    elif mode=="euclidean": # ユークリッド距離
        for x in X:
            s+=x**2

        s=sqrt(s)
    elif mode=="chebyshev": # チェビシェフ距離
        for x in X:
            s=max(s,abs(x))

    return s

print(distance(X,mode="manhattan"))
print(distance(X,mode="euclidean"))
print(distance(X,mode="chebyshev"))