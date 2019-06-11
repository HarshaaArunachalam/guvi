N,K=input().split()
Na=input().split()
new=[]
for i in Na:
    if((int (i)%2)==1):
        new.append(i)
print(new[int(K)-1])
