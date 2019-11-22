##### 解けた #####

import numpy as np

w=np.asarray(list(input()))
NGflag=False

for u in np.unique(w): # 各ユニークワードについて
    if len(np.where(w==u)[0])%2==1: # 奇数個の場合、ダメ
        NGflag=True

if NGflag==True: # ダメな場合
    print("No")
else: # よい場合
    print("Yes")