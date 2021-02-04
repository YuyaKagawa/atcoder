##### 解けた

S=input()
T=input()

min_sum_d=len(T) # 違う文字数の最小値

for ind_s in range(0,len(S)-len(T)+1):
    sum_d=0 # 違う文字の数

    for ind in range(0,len(T)):
        if S[ind_s+ind]!=T[ind]:
            sum_d+=1

    min_sum_d=min(min_sum_d,sum_d) # 最小値の更新

print(min_sum_d)