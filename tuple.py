a=[10,20,30]    #list type
b=(10,30,40)    #tuple type
a[1]=5
print(a)
#b[1]=15     #tuple cannot change the element
print(b)

#creating tuple using function:
    #tuple
a=tuple(x*2 for x in range(1,10,1))
print(a)

#changing elements in tuples:

c=list(b)   #convert tuple into list
print(c)
c[1]=15     #change the element
c=tuple(c)  #again convert list into tuple
print(c)

#accessing single element in tuple:

print(c[2])

# adding two tuples:

a=(11,12,13,14)
d=a+b
print(d)

#unpacking tuple:

a=(10,20,30)
(b,c,d)=(10,20,30)
#(b,c,d)=a
print(a,"\n",b,"\n",c,"\n",d)

#count(),index(),min()and max() in tuple:

a=(1,2,3,4,5,3,2,1)
print(a.count(2))
print(a.index(5))
print(min(a))
print(max(a))

