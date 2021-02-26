import math

X=input() # 文字列X
M=int(input()) # 整数M
count=0 # 個数のカウント

bmax=math.floor(math.log(M,int(max(X))+1)) # 基数として最大の値

print("bmax = ",bmax)

for b in reversed(range(2,bmax+1)):
    print(b)





for i in range(1,10):
    b=int(max(X))+i # b進数
    xb=0 # Xがb進数で表わされていると考えたときに、十進数で表した値

    for ind in range(0,len(X)): # 各桁について
        xb+=int(X[ind])*(b**ind) # 足し合わせてゆく

    print("b, xb = ",b,xb)

    if xb>M:
        break
    else:
        count+=1

print("count = ",count)

