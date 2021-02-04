##### 解けた

N=int(input())
A=list(map(int,input().split(" ")))
B=list(map(int,input().split(" ")))

s=0 # 和

for n in range(N):
    s+=A[n]*B[n]

if s==0:
    print("Yes")
else:
    print("No")