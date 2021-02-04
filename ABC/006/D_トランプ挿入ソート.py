##### 解けてない #####

import numpy as np

N=int(input())
C=[] # カードのリスト
# Cr=np.arange(1,N+1) # 理想の番号

# 入力を受け取ってカードのリストを作る
for n in range(N):
    C.append(int(input())-1)

count=0 # 操作した回数のカウント

for n in range(N):
    print("C = ",C)
    print("n, C[n] = ",n,C[n])

    if C[n]!=n:
        count+=1

        # Ct=C.copy()

        print("need to change, n={}, C[n]={}, C[C[n]]={}".format(n,C[n],C[C[n]]))

        C=C[:n]+C[n+1:C[n]+1]+[C[n]]+C[C[n]+1:]
        print("C after change, ",C)
        # Ct[Ct[n]]

        # C.pop(np.where(np.array(C)==(n))[0])
        # C.pop()
        # C=C[:n]+[n]+C[n:]

print(count)