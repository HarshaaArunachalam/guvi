string=input()
count=0
for j in string:
    if(j.isalpha()!=True and j.isdigit()!=True):
        count=count+1
print(count)
