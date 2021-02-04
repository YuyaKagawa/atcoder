##### 解けた #####

N,M=list(map(int,input().split(" ")))
OKflag=False # 解を見つけたことを示すフラグ

if M<N*2 or M>N*4: # もし足の本数が明らかに少ない、もしくは明らかに多い場合
    print("-1 -1 -1")
else:
    for x in range(0,N+1): # xについて調べてゆく
        y=float(4*N-M-2*x)
        z=float(N-x-y)

        # もしyとzが0以上の整数の場合
        if y>=0 and y.is_integer() and z>=0 and z.is_integer():
            OKflag=True       
            break
    
    if OKflag: # もし解がある場合
        print(x,int(y),int(z))
    else:
        print("-1 -1 -1")
    