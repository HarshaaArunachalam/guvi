N,K=input().split()
N=int(N)
K=int(K)
difference=abs(N-K)
if((difference%2)==0):
    print("even")
else:
    print("odd")
