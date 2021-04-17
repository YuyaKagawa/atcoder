

A,B=list(map(int,input().split(" ")))

v=B//2 # 最大の最大公約数の候補

if v>=A: # もしこの候補が範囲内にある場合、これが答え
    print("easy, ",v)
else: # もし範囲内にない場合、頑張って求めよう
    





for b in reversed(range(A+1,B+1)):
    print(b)


# def gcd(x,y):
#     """
#     2つの整数の最大公約数を求める関数
#     x<yを想定
#     """

#     if y%x==0: # もしyがxで割り切れる場合、xが最大公約数となる
#         v=x
#     else:
#         a=x
#         b=y 
#         r=1 # 初回のあまりはプログラムの都合上適当に
#         rp=r # 以前の剰余

#         while r>0:
#             q=b//a
#             r=b%a

#             b=a
#             a=r

#             if r==0:
#                 v=rp
#                 break
#             else:
#                 rp=r

#     return v

# maxgcd=1 # 最大の、最大公約数

# for a in range(A,B):
#     for b in range(a+1,B+1):
#         v=gcd(a,b)

#         # print("a = {}, b = {}, gcd = {}".format(a,b,v))

#         if v>=maxgcd:
#             maxgcd=v
#             ab=[a,b]

# print(maxgcd,ab)