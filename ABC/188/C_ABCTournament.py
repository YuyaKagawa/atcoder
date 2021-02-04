##### 解けた

N=int(input()) # 選手の数
A=list(map(int,input().split(" "))) # 強さのリスト

n1=max(A) # 優勝するやつの値
n1i=[i for i,j in enumerate(A) if j==n1][0] # 優勝するやつのインデックス

if n1i<2**(N-1):
    n2=max(A[2**(N-1):]) # 準優勝するやつの値、後半
else:
    n2=max(A[:2**(N-1)]) # 準優勝するやつの値、前半

n2i=[i for i,j in enumerate(A) if j==n2][0] # 準優勝するやつのインデックス

print(n2i+1)