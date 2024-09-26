#types of function
'''
    1.user defined function
    2.recursive function
    3.lambda function
    4.built-in function(type(),index(),len(),input(),count(),id()....)
'''
#user defined & recursive function:
'''def add():
    print("Hello")
    x=int(input("Enter the X value :"))
    if x==1:
        add()
    else:
        print("bye")
add()'''


#lambda function:

'''x=lambda a:a**2
print(x(5))
c=lambda a,b,d:a+b+d
print(c(5,4,3))'''


#Returning value from function:

def add():
    x=int(input("Enter x value :"))
    y=int(input("Enter y value :"))
    return(x,y)
a,b=add()
print(a+b)

    
