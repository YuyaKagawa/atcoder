##### 解けた #####

import numpy as np

N=int(input()) # 雨の数
R=[] # 雨のリスト
Rc=[] # 5分単位に直した雨のリスト

# 入力を受け付ける
for _ in range(N):
    R.append(list(map(int,input().split("-"))))

Rc=np.asarray(R)
Rc[:,0]=Rc[:,0]//10*10+Rc[:,0]%10//5*5 # スタートを前倒しの5分単位に
Rc[:,1]=Rc[:,1]//10*10+(Rc[:,1]%10>0).astype(int)*(Rc[:,1]%10//6+1)*5 # エンドを後ろ倒しの5分単位に
Rc[:,1]+=(Rc[:,1]%100==60).astype(int)*40 # エンドの分が60の場合、1時間足して分を00に
Rc=Rc[np.argsort(Rc[:,0])] # 開始時刻でソートする
s,e=-1,-1 # 最初のs,e

# 各雨について
for i in range(len(Rc)):
    if i==0: # 最初だけ
        s,e=Rc[i][0],Rc[i][1] # s,eを設定して次へ
        continue

    rc=Rc[i] # 今回の雨

    if e<rc[0]: # もし今回の雨の開始が前回の雨の終了よりも後の場合
        print("{:04d}-{:04d}".format(s,e))
        s,e=rc[0],rc[1] # s,eを更新
    else: # もし今回の雨の開始が前回の雨の期間ないの場合
        e=max(e,rc[1]) # 終わりを更新

print("{:04d}-{:04d}".format(s,e)) # 最後に出力