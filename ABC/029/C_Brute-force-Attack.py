from itertools import product

N=int(input())
P=list(product(["a","b","c"],repeat=N)) # 順列

for p in P:
    print("".join(p))