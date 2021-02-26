##### 解けた

def cal_K(n):
    """
    入力のnについてのKaprekar Numberを求める関数
    """

    g1=int("".join(sorted(str(n),reverse=True)))
    g2=int("".join(sorted(str(n),reverse=False)))

    return g1-g2

N,K=list(map(int,input().split(" "))) # a0とK番目
n=N

for _ in range(K):
    n=cal_K(n)

print(n)