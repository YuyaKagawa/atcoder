##### 解けた

# Nはバッテリー容量
# Mはカフェを訪れる回数
# Tは帰宅する
N,M,T=list(map(int,input().split(" ")))
n=N # バッテリーの残量、容量とは違う
b_last=0 # 最後にカフェを出た時刻
flag_NG=False # バッテリーの残量が一回でも0になったかどうか

for i in range(M): # 各カフェ
    a,b=list(map(int,input().split(" ")))
    n-=(a-b_last) # カフェに入るまでに消費

    if n<=0: # バッテリーの残量が0以下になったら
        flag_NG=True # フラグをオン
        break
    
    n=min(n+(b-a),N) # カフェで充電
    b_last=b # 最後にカフェを出た時刻

# 最後のカフェを出て、時刻Tまでの消費
n-=(T-b_last)

if n<=0: # バッテリーの残量が0以下になったら
    flag_NG=True # フラグをオン

# 最後の判定
if flag_NG!=True: # 0より大きいのを保てる場合
    print("Yes")
else: # 0以下になる場合
    print("No")