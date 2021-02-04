##### 解けてない #####

import numpy as np

N=int(input())
NG1=int(input())
NG2=int(input())
NG3=int(input())
NG=np.array([NG1,NG2,NG3])
cond1=(len(np.unique(NG))==3) and NG.max()==(NG.min()+2) # 3つ連続でつながっている場合
cond2=(NG.min()<=N) # NG地帯がスタートから先にある場合
cond3=(N in NG) # スタート地点がすでにNG
cond4=(N>297)

if  (cond1 and cond2) or cond3: # NGに突っ込んでしまうか、手数が足りない場合
    print("NO")
else:
    print("YES")