##### 解けてない #####

import re

s=input()
k=int(input())
pcand=[] # パスワードの候補のリスト

for i in range(len(s)-k+1):
    p=s[i:i+k]
    matches=re.finditer(p,s)

    print(len(list(matches)))