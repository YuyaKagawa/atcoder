##### 途中 #####

import string
import numpy as np
from itertools import combinations

def get_q():


N,Q=list(map(int,input().split(" ")))
icand=[[i for i in range(N)] for _ in range(N)] # 番号の候補
A=string.ascii_uppercase[:N] # アルファベットの候補
Qcand=list(combinations(A,2)) # クエリの候補

for q in Qcand:
    print("? "+"".join(q))
    get_q(input())





# print(Qcand)

# for _ in range(5):




#     alllen=[len(icand[i]) for i in range(len(icand))]
#     print(alllen)

#     if sum(alllen)==N:
#         break


