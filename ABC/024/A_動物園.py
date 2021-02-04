##### 解けた #####

A,B,C,K=list(map(int,input().split(" ")))
S,T=list(map(int,input().split(" ")))

print(A*S+B*T-int((S+T)>=K)*C*(S+T))