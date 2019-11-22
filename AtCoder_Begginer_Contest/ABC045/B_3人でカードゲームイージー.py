##### 解けた #####

dic={"a":0,"b":1,"c":2} # 文字→数字
dicr={0:"a",1:"b",2:"c"} # 数字→文字

Sa=input()
Sb=input()
Sc=input()
S=[Sa,Sb,Sc] # リストにしておく
i=0 # 最初はA

while True:
    if len(S[i])==0: # 空になったら表示して終了
        print(dicr[i].upper()) # 表示
        break

    card=S[i][0] # カードを取得
    S[i]=S[i][1:] # 先頭を削る
    i=dic[card] # 番を更新