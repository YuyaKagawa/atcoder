S=input()
N=int(input())

# 並び替える
for _ in range(N):
    l,r=list(map(int,input().split(" "))) # 左端と右端
    l,r=l-1,r-1 # 1ずれているのを修正

    S=S[:l]+S[l:r+1][::-1]+S[r+1:] # 並び替える

print(S)

