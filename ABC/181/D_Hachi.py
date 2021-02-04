##### 解けた、解説見た

from collections import Counter

S=input() # 数字列
c=Counter(S) # Sの中の文字のカウント
flag_8=False # 8の倍数であるかどうかのフラグ

if len(S)<=2: # 2桁以下の場合
    if int(S)%8==0 or int(S[::-1])%8==0: # 8の倍数の場合
        flag_8=True
else: # 3桁以上の場合
    for i in range(112,1000,8): # 各8の倍数について
        if not Counter(str(i))-c: # 形成できる場合
            flag_8=True
            break

if flag_8==True:
    print("Yes")
else:
    print("No")

#######################################################
# 自力実装
# from itertools import permutations
# for p in permutations(S,len(S)): # 各順列
#     # n="" # これから作成する文字列
#     n="".join(p)

#     if int(n)%8==0: # 8の倍数の場合
#         flag_8=True
#         break

# for p in permutations(S,3): # 各順列
#     # n="" # これから作成する文字列
#     n="".join(p)

#     if int(n)%8==0: # 8の倍数の場合
#         flag_8=True
#         break

