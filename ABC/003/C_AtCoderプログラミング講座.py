##### 解けた #####

N,K=list(map(int,input().split(" ")))
R=list(map(int,input().split(" ")))
rate=0.0 # レート、最初は0

for r in sorted(R)[-K:]:
    rate=(rate+r)/2 # レートの更新

print(rate)