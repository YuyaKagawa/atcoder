##### 解けた #####

A,B,C,D=list(map(int,input().split(" ")))

if B/A>D/C:
    print("TAKAHASHI")
elif B/A<D/C:
    print("AOKI")
else:
    print("DRAW")