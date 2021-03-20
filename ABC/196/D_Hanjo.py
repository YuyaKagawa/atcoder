##### 解けた！！！

# 方針としては、1枚ずつ(2x1)の畳を敷き詰めていって、可能性を列挙しましょうか。

from itertools import combinations

H,W,A,B = list(map(int,input().split(" ")))

Se = list() # 始点と終点のタプルの集合

# (2x1)の畳の敷き詰め方としてありえるものの列挙
for row in range(0,H):
    for col in range(0,W):
        st = [row,col]

        if (row+1)<H:
            en = [row+1,col]
            Se.append([st,en])

        if (col+1)<W:
            en = [row, col+1]
            Se.append([st,en])

C = list(combinations(Se,A))

count=0

for c in C:
    flagNG = False

    for p1 in range(len(c)-1):
        for p2 in range(p1+1,len(c)):
            pp1 = c[p1]
            pp2 = c[p2]

            if (pp1[0] in pp2) or (pp1[1] in pp2):
                flagNG=True

            if flagNG==True:
                break
        
        if flagNG==True:
            break

    if flagNG==False:
        count+=1

print(count)