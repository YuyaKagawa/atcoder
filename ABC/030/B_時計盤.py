##### 解けた #####

n,m=list(map(int,input().split(" ")))
nd=n%12*30 # まず00分のときの短針の角度を算出
nd+=30*m/60 # 次にm分のときの傾きを加算
md=m/60*360 # m分のときの長針の角度を算出

print(min(abs(nd-md),360-abs(nd-md)))