a=int(input("enter the x:"))
b=int(input("enter the y:"))
c=int(input("enter the c:"))
import cmath
d=cmath.sqrt(b*b-4*a*c)
x=-b+d/2*a
y=-b-d/2*a
print("The solution are:",x,y)
   
