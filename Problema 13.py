s=0
nrelem=0
x=int(input("Start: "))
while x!=0:
    s+=x
    nrelem+=1
    x=int(input())

medie= float(s/nrelem)
print("Suma =", s)
print("Media =", medie)