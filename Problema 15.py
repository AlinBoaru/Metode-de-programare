v=[]
for i in range(1,9,1):
    x=int(input("V[" + str(i) + "] ="))
    v.append(x)

for i in range (7):
    for j in range(7-i):
        if v[j] > v[j+1]:
            v[j], v[j+1] = v[j+1], v[j]

for i in range(8):
    print(v[i], end=" ")