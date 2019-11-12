##### 解けてない #####

N,T=list(map(int,input().split(" ")))
d="close" # ドアが開いているかどうか、Closeは閉じていてOpenは開いている
t=0 # ドアが開いていた時間の合計

for _ in range(N):
    A=int(input())

    if d=="close":
        d="open"
