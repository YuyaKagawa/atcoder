##### 解けた #####

import numpy as np

T=int(input()) # 待たせてよい時間の長さ
N=int(input()) # たこ焼きの数
A=np.asarray(list(map(int,input().split(" ")))) # たこ焼きのリスト
M=int(input()) # 客の数
B=np.asarray(list(map(int,input().split(" ")))) # 客のリスト
NGflag=False # 不都合な場合のフラグ

if N<M: # たこ焼きの数<客の数の場合、全員には提供できない
    print("no")
else: # たこ焼きの数<客の数の場合、全員に提供できる
    for b in B: # 客についてみてゆく
        eat=np.where((A>=b-T)&(A<=b))[0] # 食べられるたこ焼きのリスト

        if len(eat)>0: # 1個以上食べられるなら
            A=np.delete(A,eat[0]) # 最初の1個を食べる
        else: # 食べられるものが無い場合
            NGflag=True
            break

    if NGflag: # もしどこかで提供できなかった場合
        print("no")
    else: # 全員に提供できた場合
        print("yes")


