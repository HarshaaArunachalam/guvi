import math
N,K=input().split()
N=int(N)
K=int(K)
product=N*K
s=math.sqrt(product)
if(product==(s*s)):
    print("yes")
else:
    print("no")
