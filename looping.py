'''a=5
for i in range(a,10,1):
    print(i)
    
b=5
while(b<10):
    print(b)
    b=b+1'''

a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter end value"))

'''while(a<c):
    print(a,"x",b,"=",a*b)
    a+=1'''
for i in range(a,c,1):
    print(i,"x",b,"=",i*b)

