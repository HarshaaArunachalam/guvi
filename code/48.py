N=int(input())
Na=list(input().split())
sum=0

for i in range(len(Na)):
    sum=sum+int(Na[i])
print(sum//N)
