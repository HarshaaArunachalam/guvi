N=int(input())
Na=input().split()
Na=list(Na)
for i in range(0,N-1):
    if Na[i]>Na[i+1]:
        print(i)
