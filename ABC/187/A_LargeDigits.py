##### 解けた

A,B=input().split(" ")

sa=sum(list(map(int,list(A)))) # Aの各桁の和
sb=sum(list(map(int,list(B)))) # Bの各桁の和

print(max(sa,sb))