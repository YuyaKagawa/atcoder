##### 解けた

N=int(input()) # 文字列の数
Sn=set() # !から始まる文字列の集合
Sp=set() # !から始まらない文字列の集合

for n in range(N):
    s=input() # 入力文字列

    if s[0]=="!": # !から始まる
        Sn.add(s)
    elif s[0]!="!": # !から始まらない
        Sp.add(s)


flag_e=False # 不満な文字列が存在するフラグ

for sp in Sp: # 各"!から始まらない文字列の集合"の要素について
    if "!"+sp in Sn: # もし!から始まる文字列の集合に相当するものがある場合
        print(sp) # 表示
        flag_e=True # フラグをオンに
        break

if flag_e==False: # もしフラグがオフなら
    print("satisfiable")
