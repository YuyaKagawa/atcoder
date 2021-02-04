##### 解けた、ググった

from math import floor,sqrt

N=int(input()) # 数
l=[] # 順番通りに表示するためのリスト

for n in range(1,floor(sqrt(N))+1): # √Nまでの探索
    if N%n==0: # 割り切れる場合
        print(n) # 表示

        if n**2!=N: # 平方根ではない場合
            l.append(int(N/n)) # リストに追加

for x in l[::-1]: # 逆順に表示
    print(x)