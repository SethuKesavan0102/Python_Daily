'''a={'a1':{'Name':'raja','age':20,'city':'Madurai'},
   'a2':{'Name':'ragu','age':21,'city':'Madurai'},
   'a3':{'Name':'ravi','age':22,'city':'Madurai'}
   }
#b=a.values()
#print(b)
o=input("Enter Name :")
if o  a.values():
    #c=a[o]
    print(o)'''
d={}
z={}
for i in range(3):
    y=int(input("Enter Roll No:"))
    name=input("Enter the Name :")
    age=input("Enter the Age :")
    class_1=input("Enter the Class :")
    d.update({y:{'Name':name,'Age':age,'Class':class_1}})
    z[name]=y
print(d)

o=input("Enter name :")
#if o==d[y]['Name']:
    #print('Name :',d[y]['Name'],"\n"'Age :',d[y]['Age'],"\n"'Class :',d[y]['Class'])
if o in z:
    s=z[o]
    a=d[s]
    print('Roll No:', s)
    print('Name:', a['Name'])
    print('Age:', a['Age'])
    print('Class:', a['Class'])
    
