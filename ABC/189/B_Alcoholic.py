##### 解けた

N,X=list(map(int,input().split(" ")))
X=X*100
a=0.0 # アルコール飲んだ量
flagD=False # 酔っ払ったかどうかのフラグ

for n in range(N):
    v,p=list(map(int,input().split(" ")))
    a+=v*p # 累計のアルコール飲んだ量を増やす

    if a>X: # 限界を超えたとき、終了
        flagD=True # 酔っ払った
        print(n+1)
        break

if flagD==False:
    print(-1)

