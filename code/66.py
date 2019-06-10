number=int(input())
x=0
y=1
while y<=number:
    if(number%y)==0:
        x=x+1
    y=y+1
if(y==2):
    print("yes")
else:
    print("no")
