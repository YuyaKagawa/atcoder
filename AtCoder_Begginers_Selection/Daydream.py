##### 解けた #####

S=input() # 入力文字列

# 方策: 後ろの方から見ていって確定させてゆく
while len(S)>0:
    if S[-5:]=="dream": # 最後の5文字が"dream"の場合
        S=S[:-5]
    elif S[-5:]=="erase": # 最後の5文字が"erase"の場合
        S=S[:-5]
    elif S[-7:]=="dreamer": # 最後の7文字がdreamerの場合
        S=S[:-7]
    elif S[-6:]=="eraser": # 最後の6文字が"eraser"の場合
        S=S[:-6]
    else: # もし当てはまらなかったら"NO"と表示して終了
        print("NO")
        break

if len(S)==0: # もし最後までいけたら"YES"と表示する
    print("YES")
