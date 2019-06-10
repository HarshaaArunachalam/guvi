word=list(input())
mid=len(word)//2
if ((len(word)%2)==0):
    word[mid]='*'
    word[mid-1]='*'
else:
    word[mid]='*'
for i in word:
    print(i,end='')
