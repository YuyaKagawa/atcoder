##### 解けた #####

N=int(input())
K=int(input())
X=int(input())
Y=int(input())

print(int(N<K)*(N*X)+int(N>=K)*(K*X+(N-K)*Y))