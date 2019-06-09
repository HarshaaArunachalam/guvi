N,K=input().split()
Na=input().split()
a=0
for j in Na:
    if(int(j)%int(K)==0):
       a=j 
if(a==K):
    print("yes")
else:
    print("no")
