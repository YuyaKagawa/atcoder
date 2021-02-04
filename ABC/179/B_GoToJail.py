##### 解けた

N=int(input())
combo=0 # コンボ

for _ in range(N):
    D1,D2=list(map(int,input().split(" ")))

    if D1==D2:
        combo+=1
    else:
        combo=0

    if combo>=3:
        break

if combo>=3:
    print("Yes")
else:
    print("No")