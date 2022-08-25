import math
a=int(input("digite o valor de a:"))
b=int(input("digite o valor de b:"))
c=int(input("digite o valor de c:"))
delta = b**2 - 4*a*c

if (delta >= 0):
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b-math.sqrt(delta))/2*a
    print("Raiz x1= %.2f" % round(x1,2))
    print("Raiz x2= %.2f" % round(x2,2))
else:
    delta=delta*(-1)
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b-math.sqrt(delta))/2*a
    print("Raiz x1= %.2f" % round(x1,2),"i")
    print("Raiz x2= %.2f" % round(x2,2),"i")
    
