N,sym,K=input().split()
N=int(N)
K=int(K)
if(sym=='/'):
    print(N//K)
else:
    print(N%K)
