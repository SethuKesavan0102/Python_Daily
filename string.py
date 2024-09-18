a="Hello"
b="World"

#concadination(+)
c=a+b
print(c)

#append(+)
d=a+"World"

#repeat(*)
print(a*4)

#built-in functions for string

    #len()
print(len(a))

    #upper()
print(a.upper())

    #lower()
print(a.lower())

    #capitalize()
print(a.capitalize())

    #ord()
a='A'
print(ord(a))

    #id()
print(id(a))

    #string slicing(cut) variable_name [start:end]
b='this is a python'
x=b[1:4]
print(x)
x=b[:8]
print(x)
x=b[3:]
print(x)
    #string sride slicing(cut) variable_name [start:end:step]
a="Hello World" #we can use slicing method in list.
print(a[::3])

a[2]="a"
print(a)


