import numpy as np

N=int(input()) # 数列の長さ
An=np.asarray(list(map(int,input().split(" ")))).reshape(-1,1)
Bn=np.asarray(list(map(int,input().split(" ")))).reshape(1,-1)
thre=1000000000+7 # でかすぎるので小さくするために
Cn=np.dot(An,Bn)
Cn1=Cn//thre # 商
Cn2=Cn%thre # 余り
mc=0

for j in range(0,N):
    # c1=Cn1[:j+1,j].reshape(-1,)
    # c2=Cn2[:j+1,j].reshape(-1,)
    mc=max(mc,(Cn1[:j+1,j].reshape(-1,)*thre+Cn2[:j+1,j].reshape(-1,)).max())
    print(mc)




    # print(a.shape,b.shape)
    
    # print((c1*thre+c2).shape)

    # print(a*thre+Cn2[:j+1,j].reshape(-1,)).shape)



# A=list(map(int,input().split(" ")))
# B=list(map(int,input().split(" ")))


# print(Cn.shape)
# print(Cn[0,:])




    # for i in range(0,j+1):
    #     print(i,j,Cn[i,j])




# for n in range(N):
#     print(Cn[:n+1,:n+1])













ma=0
# mb=0
mc=0

for j in range(0,N):
    # mb=max(mb,B[j])
    b=B[j]

    for i in range(0,j+1):
        a=A[i]
        ma=max(ma,A[i])
        # print(i,j)

        # c=a*b
        # print("c = ",c)
  
    mc=max(mc,ma*b)
    # print("mc = ",mc)
    print(mc)

    # mc=max(mc,c)

#####################
### テスト用
for j in range(0,N):
    # mb=max(mb,B[j])
    b=B[j]

    for i in range(0,j+1):
        a=A[i]
        c=max(a,b)

        # ma=max(ma,A[i])
        # print(i,j)

        # c=a*b
        # print("c = ",c)
  
    # mc=max(mc,ma*b)
    # print("mc = ",mc)
    # print(mc)
        
ma=min(A)
mb=min(B)

for i in range(0,N):
    A[i]=A[i]%ma

for j in range(0,N):
    B[i]=B[i]%mb
    
