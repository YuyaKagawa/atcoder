from math import gcd

T=int(input()) # テストケースの数


for _ in range(T):
    # N: 椅子の数、S: 最初の高橋くんの位置（玉座からのインデックス）、K: 何個移動するか
    N,S,K=list(map(int,input().split(" "))) 
    n,s,k=N,S,K


    g=gcd(k,n)

    print("n,s,n-s,k,g = ",n,s,n-s,k,g)

    # if (N-S)%g!=0:
    #     print(-1)
    #     break
    # else:
    #     k=k/g
    #     n=n/g
    #     l=(n-s)/g


    # r=[]
    # s=S
    # num=0
    # flag_g=False

    # bool_n=(N%2==1)
    # bool_ns=((N-S)%2==1)
    # bool_K=(K%2==1)
    
    # if N==K:
    #     pass
    # elif bool_n==False and bool_ns==True and bool_K==False:
    #     pass
    # else:
    #     while True:
    #         s=(s+K)%N
    #         num+=1

    #         if s==0:
    #             flag_g=True
    #             break
    #         if s in r:
    #             flag_g=False
    #             break

    #         r.append(s)


    # if flag_g==True:
    #     print(num)
    # elif flag_g==False:
    #     print(-1)


