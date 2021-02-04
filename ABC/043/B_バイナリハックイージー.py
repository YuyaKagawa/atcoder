##### 解けた #####

S=input()
A=[""]

for s in S: # 入力の文字列1文字ずつ見てゆく
    if s in ["0","1"]: # もし0か1の場合、それを追加
        A.append(s)
    elif s=="B": # もしバックスペースの場合、1文字削除
        if len(A)>=1: # 長さが1以上の場合のみ削除
            A.pop(-1)

print("".join(A))