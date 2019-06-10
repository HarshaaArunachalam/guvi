import math
N,K=input().split()
N=int(N)
K=int(K)
print((N*K)//math.gcd(N,K))
