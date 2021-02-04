##### 部分点 #####

from math import factorial

X,Y=list(map(int,input().split(" ")))

a=(2*Y-X)/3
b=(2*X-Y)/3

if a.is_integer() and b.is_integer():
    print(int(factorial(a+b)/(factorial(a)*factorial(b))%1000000007)) # 順列の数を計算する
else:
    print(0)