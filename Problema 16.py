a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
import math

d= b*b -4*a*c
if d<0:
    print("Delta < 0")
    SystemExit
else:
    x1= -b + math.sqrt(d)
    x2= -b - math.sqrt(d)
    print("x1 = ", x1, "x2 =", x2)