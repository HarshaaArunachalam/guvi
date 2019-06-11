L,B,H=input().split()
L=int(L)
B=int(B)
H=int(H)
surface=2*((L*B)+(B*H)+(H*L))
volume=L*B*H
print(surface,volume)
