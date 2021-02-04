##### 解けた #####

A=int(input())
B=int(input())
C=int(input())
X=int(input())

count=0 # 合計金額がX円になる通り

# for文で探してゆく
# 最大で50*50*50=125,000回のループ
for ai in range(A+1):
    for bi in range(B+1):
        for ci in range(C+1):
            if 500*ai+100*bi+50*ci==X:
                count+=1

print(count)