words=input()
for i in range(0,len(words)):
    if (i%2)==0:
        print(words[i],end="")
print(" ",end="")
for i in range(0,len(words)):
    if (i%2)!=0:
        print(words[i],end="")
