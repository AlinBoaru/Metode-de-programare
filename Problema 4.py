a=int(input("Primul numar: "))
b=int(input("Al doilea numar: "))

while a!=b:
    if a>b: a=a-b
    else: b=b-a

print(a," este cmmdc")