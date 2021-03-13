A,B,W=list(map(int,input().split(" ")))

if W<A: # ありえない
    print("UNSATISFIABLE")
elif A<=W<=B:
    print(1)
else:
    print(W//B+int(W%B!=0))