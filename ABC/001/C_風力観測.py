##### 解けた #####

from decimal import * # 後に四捨五入を扱うために

# 風向きのリスト
DD=[
    "N","NNE","NE","ENE",
    "E","ESE","SE","SSE",
    "S","SSW","SW","WSW",
    "W","WNW","NW","NNW",
    "N"
]

Deg,Dis=list(map(int,input().split(" ")))
Deg=Deg*10+1125 # 後に誤差で苦しまないようにintで
Dir=DD[int(Deg//2250)] # 風向き
Dis=Dis*10 # 後に誤差で苦しまないようにintで
Dis=Decimal(str(Dis/60)).quantize(Decimal("0"),rounding=ROUND_HALF_UP) # これが本当の四捨五入です

# 風力
if Dis<=2:
    Dir="C"
    W="0"
elif Dis<=15:
    W="1"
elif Dis<=33:
    W="2"
elif Dis<=54:
    W="3"
elif Dis<=79:
    W="4"
elif Dis<=107:
    W="5"
elif Dis<=138:
    W="6"
elif Dis<=171:
    W="7"
elif Dis<=207:
    W="8"
elif Dis<=244:
    W="9"
elif Dis<=284:
    W="10"
elif Dis<=326:
    W="11"
else:
    W="12"

print(Dir+" "+W)