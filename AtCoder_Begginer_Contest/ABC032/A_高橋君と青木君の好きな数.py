##### 解けてない #####

a=int(input())
b=int(input())
n=int(input())

# n以上の整数を見ていって、aとbで割り切れたら表示して終了
for i in range(n,20001):
    if i%a==0 and i%b==0: # aとbで割り切れる
        print(i)
        break