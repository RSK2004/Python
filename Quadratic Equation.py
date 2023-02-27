import math
a = int(input("Enter coefficient of x^2:"))
b = int(input("Enter coefficient of x:"))
c = int(input("Enter constant of x:"))
D = b*b-4*a*c
if D>0:
    root1 = (-b+D)/(2*a)
    root2 = (-b-D)/(2*a)
    print("Roots are:",root1,root2)
elif D == 0:
    root1 = -b/(2*a)
    print(root1)
else:
    realpart = -b/(2*a)
    imagpart = sqrt(-D)/(2*a)
    print("Roots are:",realpart,imagpart)
    
