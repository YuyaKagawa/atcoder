##### 解けた #####

n=int(input()) # 何番目を求めるか
prev=[0,0,1] # 3個前、2個前、1個前の値

if (n-1)<3: # もしn<3の場合、特殊な対応
    print(prev[n-1])
else: # n>=3の場合、繰り返して求めてゆく
    for _ in range(n-4):
        t=prev.copy()
        prev[2]=sum(t)%10007
        prev[1]=t[2]
        prev[0]=t[1]

    print(sum(prev)%10007)