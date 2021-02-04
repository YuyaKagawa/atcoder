##### 解けてない、オーバーフロー

from math import log,ceil,floor

X,Y,A,B=list(map(int,input().split(" ")))

n_thre1=max(0,ceil(log(B,A)-log(A-1,A)-log(X,A)+1)-1)

# print("raw = ",log(B,A)-log(A-1,A)-log(X,A)+1)

thre=X*A**n_thre1

print("Y, thre, B = ",Y,thre,B)

n_thre2=max(0,ceil((Y-thre)/B)-1)

print("raw2 = ",(Y-thre)/B,ceil((Y-thre)/B))
# print("raw = ",ceil((Y-thre)/B)-1)

# print("n_thre1, n_thre2 = ",n_thre1,n_thre2)

# print("n_thre1+n_thre2 = ",n_thre1+n_thre2)

print(n_thre1+n_thre2)

# 愚直に
# e=0
# while X<Y:
#     if X<B/(A-1): # Xが十分小さいとき、カコモンジムへ
#         X*=A
#     elif X>=B/(A-1): # Xが十分大きいとき、AtCoderジムへ
#         X+=B

#     if X<Y:
#         e+=1 # 経験値を足す

#     print(X,e)

