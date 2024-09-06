e=int(input("enter the e value"))
f=int(input("enter the f value"))
g=int(input("enter the g value"))

if(e>f):
    if(e>g):
        print("E is greater")
    else:
        print("G is greater")
else:
    if(f>g):
        print("F is greater")
    else:
        print("G is greater")

a=int(input("Enter the A value"))
b=int(input("Enter the B value"))
c=int(input("Enter the C value"))
d=int(input("Enter the D value"))
    

if(a>b):
    if(a>c):
        if(a>d):
            print("A is greater")
        else:
            print("D is greater")   
    else:
        print("C is greater")
       
    
else:
    if(b>c):
        if(b>d):
            print("B is greater")
        else:
            print("D is greater")
    else:
        print("C is greater")
