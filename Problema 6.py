x=int(input("Numar: "))
ok=1
for i in range (2,int(x/2) ,1):
    if x%i==0:
        ok=0

if ok==1: print(x," este numar prim")
else: print(x," nu este numar prim") 