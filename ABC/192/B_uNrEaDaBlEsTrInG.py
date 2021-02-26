##### 解けた

S=input() # 文字列
flagndif=False # 文字列が難しくないかどうかのフラグ

for i in range(len(S)):
    if i%2==0 and S[i].islower()==False:
        flagndif=True
    elif i%2==1 and S[i].islower()==True:
        flagndif=True

    if flagndif==True:
        break

if flagndif==True:
    print("No")
else:
    print("Yes")