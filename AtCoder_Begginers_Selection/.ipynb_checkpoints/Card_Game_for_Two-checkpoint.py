##### 解けた #####

N=int(input())
A=list(map(int,input().split(" ")))
A+=[0]*int(len(A)%2==1)
A.sort(reverse=True)

print(sum(A[::2])-sum(A[1::2]))