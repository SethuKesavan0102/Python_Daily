'''a=set({})
print(type(a))
a.add(1)
print(a)
a.add(2)
print(a)
a.add(5)
a.add(7)
a.add(8)
print(a)
b=[1,2,3,4]
a.update(b)
print(a)'''

#four method

a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
print(a.union(b))   #join two sets using union() or |
print(a.intersection(b))    #get common value using intersection() or &
print(a.difference(b))  #get remaining a value using difference() or -
print(a.symmetric_difference(b))    #get value without common value using ^


#delete the value in set
    #remove()   it can delete what we need
    #pop()      it can delete randomly
    #discard()  it can delete what we need in case that number is not means that cannot get error

