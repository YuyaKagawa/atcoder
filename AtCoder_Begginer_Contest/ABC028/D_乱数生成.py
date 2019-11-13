##### 解けてない #####

N,K=list(map(int,input().split(" ")))
p1=K/N
p2=1/N
p3=(N-K+1)/N

print("p1, p2, p3 = ",p1,p2,p3)

print(6*p1*p2*p3)