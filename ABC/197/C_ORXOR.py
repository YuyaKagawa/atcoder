##### 解けてない

N=int(input())
Ad=list(map(int,input().split(" "))) # 数列、10進表記
Ab=[] # 数列、2進表記

def deg2bin(deg):
    """
    10進表記の数字を、2進表記に変更する
    """

    d=deg # これから割ってゆく値
    b="" # 2進数を文字列で保持

    while d>=2: # dが2以上の場合
        b=str(d%2)+b
        d=d//2

    b=str(d)+b

    return b

mlen=0 # 2進表記の数字の長さの最大値

for ad in Ad:
    print("{} -> {}".format(ad,deg2bin(ad)))
    ab=deg2bin(ad)

    mlen=max(mlen,len(ab))

    Ab.append(deg2bin(ad))

### 0埋め
for i in range(len(Ab)):
    Ab[i]="0"*(mlen-len(Ab[i]))+Ab[i]

print(Ab)