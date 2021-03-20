##### 解けた

N=input() # 入力（文字列）
Ni=int(N) # 入力（数字）

if len(N)<2: # 1桁の数字の場合、なし
    print(0)
else: # 2桁以上の場合
    # ある桁数dを考える、2*dとなりうる

    count = 0 # カウント

    for d in range(1,(len(N)-1)//2+1): # その桁数未満の偶数桁数について
        count += 9*10**(d-1)

    if len(N)%2==0: # 偶数桁数の場合、同じ桁数についても見る
        d=len(N)//2
        minn = 10**(d-1)
        maxn = (10**d)-1 

        for n in range(minn,maxn+1):
            nn = int("{}{}".format(n,n))

            if nn<=Ni:
                count+=1
            else:
                break

    print(count)
