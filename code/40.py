N=int(input())
x=0
y=1
for j in range(0,N):
    print(y,end=" ")
    z=x+y
    x=y
    y=z
