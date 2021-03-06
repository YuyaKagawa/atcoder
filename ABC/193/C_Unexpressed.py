##### 解けた

import math

N=int(input()) # 整数
S=set() # 集合

if N<4: # N<4の場合、答えはN
    print(N)
else: # N>=4の場合
    for a in range(2,math.floor(math.sqrt(N))+1):
        for b in range(2,math.floor(math.log(N,a))+1):
            n=(a**b) # 値の計算

            if n<=N and n not in S: # もしa**bがN以下で、まだ集合に追加されていない場合
                S.add(n) # 集合に追加する
            elif a**b>N: # もしNを上回ったら
                break # 次の数字へ

    print(N-len(S)) # 答えの表示

