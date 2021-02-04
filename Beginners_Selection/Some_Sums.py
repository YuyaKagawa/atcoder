##### 解けた #####

N,A,B=list(map(int,input().split(" ")))
sumall=0 # 全ての総和

# 1<=N<=10,000 より最大10,000回のループ
for n in range(1,N+1):
    sumn=sum(list(map(int,list("{:05d}".format(n)))))
    
    if sumn>=A and sumn<=B:
        sumall+=n

print(sumall)