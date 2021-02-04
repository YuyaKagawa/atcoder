##### 解けた、テストケース見た

Nl=list(input()) # 数字(list,str)
Nl3=[int(e)%3 for e in Nl] # 数字を3で割ったあまり(list,int)
Nl3s=set(Nl3) # 数字を3で割ったあまり(set,int)
Ni=int("".join(Nl)) # 数字(int)
k=len(Nl) # Nの桁数

r=Ni%3 # 3で割ったあまり
num12=len([e for e in Nl3 if e==1]) # 1の数
num22=len([e for e in Nl3 if e==2]) # 2の数

if r==0: # もし既に3で割れる場合、0
    print(0)
elif ((r==1 and (1 in Nl3s)) or (r==2 and (2 in Nl3s))) and k>1:
    # あまりが1で1がある場合、もしくはあまりが2で2がある場合、1
    print(1)
elif ((r==2 and num12>=2) or (r==1 and num22>=2)) and k>2:
    # kも2より大きい場合、かつ
    # あまりが2で、1が2個以上ある場合、2
    # あまりが1で、2が2個以上ある場合、2
    
    print(2)
else: # 割り切れない場合、-1
    print(-1)