x=int(input())
max=x
min=x
#in enunt nu spune daca avem nr de termeni din lista, asa ca citeste din lista pana cand x=0
while x!=0:
    if x>max: max=x
    if x<min: min=x
    x=int(input())

print("MAX =", max)
print("MIN =", min)