##### 解けた

N=int(input()) # 景品の数
S=set() # 景品の集合

for _ in range(N):
    S.add(input())

print(len(S))