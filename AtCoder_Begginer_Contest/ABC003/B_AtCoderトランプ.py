##### 解けた #####

S=list(input())
T=list(input())
atnum_to=["@","a","t","c","o","d","e","r"] # @の変換先のリスト
NGflag=False # 一致しないことを示すフラグ

# 順番に見てゆく
for n in range(len(S)):
    if S[n]=="@": # Sのn番目が@の場合
        if T[n] not in atnum_to: # もしSのn番目が変換不可の場合
            NGflag=True
    elif T[n]=="@": # Tのn番目が@の場合
        if S[n] not in atnum_to: # もしSのn番目が変換不可の場合
            NGflag=True
    else: # どちらも@ではない場合
        if S[n]!=T[n]: # n番目が一致しない場合
            NGflag=True

if NGflag: # 一致しない場合
    print("You will lose")
else: # 一致する場合
    print("You can win")