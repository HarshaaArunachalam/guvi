ch=str(input())
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    if(ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U' or ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
