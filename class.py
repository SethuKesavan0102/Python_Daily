'''class student:
    name=""
    age=0
    mobile=0

sk=student()

sk.name="sk"
sk.age=20
sk.mobile=34567890
print(sk.name)
print(sk.age)
print(sk.mobile)

loki=student()

loki.name="loki"
loki.age=22
loki.mobile=98765432
print(loki.name)
print(loki.age)
print(loki.mobile)'''

#class method

'''class student:
    name=""
    age=0
    mobile=0
    def get(self):
        self.name=input("Enter the name :")
        self.age=int(input("Enter tha age :"))
        self.mobile=int(input("Enter tha mobile number :"))
    def put(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Mobile :",self.mobile)
sk=student()
sk.get()
sk.put()

loki=student()
loki.get()
loki.put()

nandha=student()
nandha.get()
nandha.put()'''

#task1

'''sprint("Welcome to All")
print("Enter your option")

class detail:
    def det(self):
        self.name=""
        self.age=0
        self.rollno=0

    def input(self):
        self.name=input("Enter the Name :")
        self.age=int(input("Enter the Age :"))
        self.rollno=int(input("Enter the RollNo :"))

    def print(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Rollno :",self.rollno)

    def program(self):
        for i in range(20):
        #while 1:
            x=int(input("1.Add Student Details,\n2.View Student Details,\nThe Given Values Must be in a Number :"))

            if x==1:
                self.input()
            elif x==2:
                self.print()
            else:
                print("Wrong")
                

            choose=input("Do You Want To Continue (Y/N):")
            if choose!="y":
                print("Exiting......bye")
                break

sk=detail()
sk.program()'''


#constructor & Destructor:

'''class person:
    def __init__(self):                     #constructor __init__
        print("Constructor is Executed")
    def __del__(self):                      #destructor __del__
        print("Destructor is Executed")

class person1:
    def hello(self):
        print("Constructor")

a1=person()
a2=person1()
a2.hello()
del a1
'''

#constructor:

'''class add:
    def __init__(self,name,age):    #only use for constructor
        self.name=name
        self.age=age
        print("name",self.name)
        print("age",self.age)
a1=add("john",23)
'''

#data member:

'''class person:
    a='Hello'   #public
    __a1='Hello1'   #private
    def add(self):
        print(self.__a1)
a3=person()
a3.add()
print(a3.a)'''

#single inheritance:

'''class person1:      #parent
    a=""
    b=0
    def get(self):
        self.a=input("Enter name :")
        self.b=input("Enter age :")

class person2(person1,person):     #child
    
    def print(self):
        print(self.a)
        print(self.b)

a1=person2()
a1.get()
a1.print()'''

#multiple inheritance:


'''class person1:      #parent
    a=""
    b=0
    def get(self):
        self.a=input("Enter name :")
        self.b=input("Enter age :")

class person:
    mark=0
    id=0
    def subn(self):
        self.mark=input("Enter mark :")
        self.id=input("Enter id :")
        
        
class person2(person1,person):     #child
    
    def print(self):
        print(self.a)
        print(self.b)
        print(self.mark)
        print(self.id)
        
a1=person2()
a1.get()
a1.subn()
a1.print()'''

#task
'''
class product:
    a=""
    b=""
    c=0
    d=0
    e=0
    def __init__(self):
        self.a=input("Enter Product Name :")
        self.b=input("Enter Product ID :")
        self.c=int(input("Enter Expiry :"))
        self.d=int(input("Enter Price :"))
        self.e=int(input("Enter Quantity :"))
#class product1(product):
    def print(self):
        print("Product Name :",self.a)
        print("Product ID :",self.b)
        print("Product Expiry :",self.c)
        print("Product Price :",self.d)
        self.f=self.d*self.e
        print("Total Price :",self.f)

#a1=product1()
a1=product()
a1.print()
'''


#task
'''
class product:
    def rice(self):
        quantity=int(input("Enter Product Quantity :"))
        print("Product_ID :12345")
        print("Product_Expiry : 20/02/2025")
        print("Product_Price : 200")
        print("product_Quantity :",quantity)
        print("Total amount:",200*quantity)

class product1:
    def wheat(self):
        quantity=int(input("Enter Product Quantity :"))
        print("Product_ID :23456")
        print("Product_Expiry : 2/08/2025")
        print("Product_Price : 100")
        print("product_Quantity :",quantity)
        print("Total amount:",100*quantity)

class product2:
    def sugar(self):
        quantity=int(input("Enter Product Quantity :"))
        print("Product_ID :34567")
        print("Product_Expiry : 4/12/2025")
        print("Product_Price : 48")
        print("product_Quantity :",quantity)
        print("Total amount:",48*quantity)


class final(product,product1,product2):
    def __init__(self):
        a=input("Enter Product Name :")
        if a=="rice":
            self.rice()
            self.__init__()
        elif a=="wheat":
            self.wheat()
            self.__init__()
        elif a=="sugar":
            self.sugar()
            self.__init__()
        else:
            print("Product Out of Stock...")

product=final()
'''


#types of inheritance:
'''
1.single
2.multiple
3.multi-level
4.hierarchical
5.hybrid
'''

#single:
'''
class parent:
    def print1(self):
        print("This is Parent class")
class child(parent):
    pass
a1=child()
a1.print1()
'''

#multiple:
'''
class parent1:
    def c1(self):
        print("This is First Parent")

class parent2:
    def c2(self):
        print("This is Second Parent")
class child(parent1,parent2):
    pass
a1=child()
a1.c1()
a1.c2()
'''

#multi-level:
'''
class parent1:
    def c1(self):
        print("This is First Parent")

class parent2(parent1):
    def c2(self):
        print("This is Second Parent")
class child(parent2):
    pass
a1=child()
a1.c1()
a1.c2()
'''

#hierarchical:
'''
class parent:
    def c1(self):
        print("this is parent")
class child(parent):
    def c2(self):
        print("this is child one")

class child1(parent):
    def c3(self):
        print("this is child two")

a1=child()
a1.c1()
a1.c2()
a2=child1()
a2.c1()
a2.c3()
'''

#hybrid:
'''
class parent:
    def c1(self):
        print("this is parent")
class child(parent):
    def c2(self):
        print("this is child one")

class child1(parent):
    def c3(self):
        print("this is child two")

class child2(child,child1):
    pass

a1=child2()
a1.c1()
a1.c2()
a1.c3()
'''


#task

'''
d={}
l1=["Name","Age","Class"]
class student:
    def __init__(self):
        for i in range(50):
            self.x=int(input("1.Enter Student Details\n2.View Details\n3.Exit"))
            if self.x==1:
                self.student_detail()
            
            elif self.x==2:
                self.view_details()
                
            elif self.x==3:
                print("Thank You")
                break
            
            else:
                print("Invalid Option")
                

    def student_detail(self):
        y=int(input("Enter Roll No:"))
        z={}
        for j in l1:
            z[j]=input(j)
            d[y]=z
        
    def view_details(self):
        p=int(input("Enter Roll No:"))
       
        if p in d:
            h=p
            c=d[h]
            print('Name :',c['Name'],"\n"'Age :',c['Age'],"\n"'Class :',c['Class'])
        else:
            print("Roll_No not found")
                          
person=student()
'''

#task
'''
d={}
l1=["Name","Age","Class"]
class student:
    def __init__(self):
        for i in range(50):
            self.x=int(input("1.Enter Student Details\n2.View Details\n3.Exit"))
            if self.x==1:
                self.student_detail()
            
            elif self.x==2:
                self.view_details()
                
            elif self.x==3:
                print("Thank You")
                break
            
            else:
                print("Invalid Option")
                

    def student_detail(self):
        y=int(input("Enter Roll No:"))
        z={}
        for j in l1:
            z[j]=input(j)
            d[y]=z
        
    def view_details(self):
        
        p=int(input("View Details By :\n1.By Name\n2.By Age\n3.By Class\n4.By Roll_No"))
        if p==1:
            o=input("Enter Name :")
            for i,b in d.items():
                if b['Name']==o:
                    print('Roll_No :',i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])
        elif p==2:
            o=input("Enter Age :")
            for i,b in d.items():
                if b['Age']==o:
                    print('Roll_No :',i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])
        elif p==3:
            o=input("Enter Class :")
            for i,b in d.items():
                if b['Class']==o:
                    print('Roll_No :',i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])
        elif p==4:
             h=int(input("Enter Roll No:"))
             if h in d:
                 c=d[h]
                 print('Name :',c['Name'],"\n"'Age :',c['Age'],"\n"'Class :',c['Class'])
        else:
            print("Invalid Option")
                          
person=student()
'''


#operator overloading:
'''
class over:
    def __init__(self):
        self.a=int(input("Enter Value :"))
    def __add__(self,b):
        return(self.a*b.a)
a=over()
b=over()
print(a+b)
'''

#Try,Except,Finally:
'''
a=int(input("Enter Value 1:"))
b=int(input("Enter Value 2:"))
try:
    print(a/b)
except Exception as e:
    print("Error Occured",e)
finally:
    print("Finished")
'''


#task
'''
d={}
l1=["Name","Age","Class"]
class student:
    def __init__(self):
        for i in range(50):
            self.x=int(input("1.Enter Student Details\n2.View Details\n3.Exit"))
            if self.x==1:
                self.student_detail()
            
            elif self.x==2:
                self.view_details()
                
            elif self.x==3:
                print("Thank You")
                break
            
            else:
                print("Invalid Option")
                

    def student_detail(self):
        y=int(input("Enter Roll No:"))
        z={}
        for j in l1:
            z[j]=input(j)
            d[y]=z
        
    def view_details(self):
        
        p=int(input("View Details By :\n1.By Name\n2.By Age\n3.By Class\n4.By Roll_No"))
        if p==1:
            o=input("Enter Name :")
            for i,b in d.items():
                if b['Name']==o:
                    print('Roll_No :',i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])

                k=input("Do you Want to Delete(Y/N):")
                if k=='y':                    
                    del d[i]
                    break
        elif p==2:
            o=input("Enter Age :")
            for i,b in d.items():
                if b['Age']==o:
                    print('Roll_No :',i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])

                k=input("Do you Want to Delete(Y/N):")
                if k=='y':                    
                    del d[i]
                    break
        elif p==3:
            o=input("Enter Class :")
            for i,b in d.items():
                if b['Class']==o:
                    print('Roll_No :',i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])

                k=input("Do you Want to Delete(Y/N):")
                if k=='y':                    
                    del d[i]
                    break
        elif p==4:
             h=int(input("Enter Roll No:"))
             if h in d:
                 c=d[h]
                 print('Name :',c['Name'],"\n"'Age :',c['Age'],"\n"'Class :',c['Class'])

             k=input("Do you Want to Delete(Y/N):")
             if k=='y':                    
                 del d[h]
                 
        else:
            print("Invalid Option")
        
                          
person=student()
print(d)

'''


#task using update():
'''
d={}

class student:
    def __init__(self):
        for i in range(50):
            self.x=int(input("1.Enter Student Details\n2.View Details\n3.Exit"))
            if self.x==1:
                self.student_detail()
            
            elif self.x==2:
                self.view_details()
                
            elif self.x==3:
                print("Thank You")
                break
            
            else:
                print("Invalid Option")
                

    def student_detail(self):
        y=int(input("Enter Roll No:"))
        name=input("Enter the Name :")
        age=input("Enter the Age :")
        class_1=input("Enter the Class :")
        d.update({y:{'Name':name,'Age':age,'Class':class_1}})


    def view_details(self):
        
        p=int(input("View Details By :\n1.By Name\n2.By Age\n3.By Class\n4.By Roll_No"))
        if p==1:
            o=input("Enter Name :")
            for i,b in d.items():
                if b['Name']==o:
                    print('Roll_No :',i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])

                k=input("Do you Want to Delete(Y/N):")
                if k=='y':                    
                    del d[i]
                    break
        elif p==2:
            o=input("Enter Age :")
            for i,b in d.items():
                if b['Age']==o:
                    print('Roll_No :',i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])

                k=input("Do you Want to Delete(Y/N):")
                if k=='y':                    
                    del d[i]
                    break
        elif p==3:
            o=input("Enter Class :")
            for i,b in d.items():
                if b['Class']==o:
                    print('Roll_No :',i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])

                k=input("Do you Want to Delete(Y/N):")
                if k=='y':                    
                    del d[i]
                    break
        elif p==4:
             h=int(input("Enter Roll No:"))
             if h in d:
                 c=d[h]
                 print('Name :',c['Name'],"\n"'Age :',c['Age'],"\n"'Class :',c['Class'])

             k=input("Do you Want to Delete(Y/N):")
             if k=='y':                    
                 del d[h]
                 
        else:
            print("Invalid Option")
        
                          
person=student()
print(d)
'''


#encapsulation:

'''a=10    #public
__a=10 `#private
_a=10   #protector'''



#task
'''
d={}
l1=["Name","Age","Class"]
class student:
    def __init__(self):
        count=0
        
        for i in range(50):
            self.x=int(input("1.Enter Student Details\n2.View Details\n3.Delete The Data\n4.Exit"))
            if self.x==1:
                self.student_detail()
                count=1
            
            elif self.x==2:
                if count==1:
                    self.view_details()
                else:
                    print("Enter Atleast One Value")
                    
                
                
            elif self.x==3:
                print("Thank You")
                break
            
            else:
                print("Invalid Option")
                

    def student_detail(self):
        y=int(input("Enter Roll No:"))
        z={}
        for j in l1:
            z[j]=input(j)
            d[y]=z
        
    def view_details(self):
        
        p=int(input("View Details By :\n1.By Name\n2.By Age\n3.By Class\n4.By Roll_No"))
        if p==1:
            o=input("Enter Name :")
            for self.i,b in d.items():
                if b['Name']==o:
                    print('Roll_No :',self.i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])
                self.delete_1()
                break

                
        elif p==2:
            o=input("Enter Age :")
            for self.i,b in d.items():
                if b['Age']==o:
                    print('Roll_No :',self.i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])

                self.delete_1()
                break
            
        elif p==3:
            o=input("Enter Class :")
            for self.i,b in d.items():
                if b['Class']==o:
                    print('Roll_No :',self.i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])

                self.delete_1()
                break
            
        elif p==4:
             self.i=int(input("Enter Roll No:"))
             if self.i in d:
                 c=d[self.i]
                 print('Name :',c['Name'],"\n"'Age :',c['Age'],"\n"'Class :',c['Class'])

             self.delete_1()
                 
        else:
            print("Invalid Option")



class student1(student):
    def delete_1(self):
        k=input("Do you Want to Delete(Y/N):")
        if k=='y':
            del d[self.i]
            
        
        
                          
#person=student()
person1=student1()
#person1.delete_1()
print(d)
'''

#encapsulation:
'''
class grandparent:
    def __init__(self):
        self._a=45          #protected
        self.__b=60         #private

class parent(grandparent):
    def add1(self):
        print(self._a)
class child(parent):
    def __init__(self):
        print("Child Constructor")
    def add1(self):
        print(self._a)

x=parent()
x.add1()
'''


#map
'''
def add1(a):
    return a*2
x=map(add1,[1,2,3,4,5,6])
print(list(x))
'''

#task
'''
d={}
#l1=["Name","Age","Class"]
class student:
    def __init__(self):
        for i in range(50):
            self.x=int(input("1.Enter Student Details\n2.View Details\n3.Delete the Student\n4.Exit"))
            if self.x==1:
                self.student_detail()
            
            elif self.x==2:
                self.view_details()

            elif self.x==3:
                self.delete_1()
                
                
            elif self.x==4:
                print("Thank You")
                break
            
            else:
                print("Invalid Option")
                

    def student_detail(self):
        y=int(input("Enter Roll No:"))
        name=input("Enter the Name :")
        age=input("Enter the Age :")
        class_1=input("Enter the Class :")
        d.update({y:{'Name':name,'Age':age,'Class':class_1}})
                
    def view_details(self):
        
        p=int(input("View Details By :\n1.By Name\n2.By Age\n3.By Class\n4.By Roll_No"))
        if p==1:
            self.o=input("Enter Name :")
            self.view_1()    
        elif p==2:
            self.o=input("Enter Age :")
            self.view_1()
        elif p==3:
            self.o=input("Enter Class :")
            self.view_1()    
        elif p==4:
            o=int(input("Enter Roll_No :"))
            if o in d:
                c=d[o]
                print('Name :',c['Name'],"\n"'Age :',c['Age'],"\n"'Class :',c['Class'])              
        else:
           print("Invalid Option")

    def view_1(self):
        for self.i,b in d.items():
                for j in b:
                    if b[j]==self.o:
                        print('Roll_No :',self.i,'\nName :',b['Name'],"\n"'Age :',b['Age'],"\n"'Class :',b['Class'])
                        

class student1(student):
    def delete_1(self):
        p=int(input("Delete Details By :\n1.By Name\n2.By Age\n3.By Class\n4.By Roll_No"))
        if p==1:
            self.o=input("Enter Name :")
            self.dele_1()  
        elif p==2:
            self.o=input("Enter Age :")
            self.dele_1()
        elif p==3:
            self.o=input("Enter Class :")
            self.dele_1()   
        elif p==4:
            self.i=int(input("Enter Roll_No :"))
            if self.i in d:
                c=d[self.i]
                print('Name :',c['Name'],"\n"'Age :',c['Age'],"\n"'Class :',c['Class'])
            s=input("Do You Want to Delete (Y/N):")
            if s=="y":
                del d[self.i]
        else:
           print("Invalid Option")
        
    def dele_1(self):
        self.view_1()
        s=input("Do You Want to Delete (Y/N):")
        if s=="y":
            del d[self.i]

            
person=student1()
print(d)
'''


#Filter
'''
def find1(x):
    a=['a','e','i','o','u','A','E','I','O','U']
    if x in a:
        return True
    else:
        return False
x=input("Enter String :")
y=filter(find1,x)
#print(list(y))
print(len(list(y)))
'''

#reduce
'''
import functools
def add1(a,b):
    #print(a,b)
    return a*2
x=functools.reduce(add1,[1,2,3,4,5,6])
print(x)
'''

#data abstraction:
'''
from abc import ABC,abstractmethod
class Person1(ABC):
    def __init__(self):
        print("Constructor")
    @abstractmethod
    def add1(self):
        pass
class person2(Person1):
    def add1(self):
        print("Person2")
class person3(Person1):
    def add1(self):          #or pass
        print("Person3")
a1=person3()
a1.add1()
a2=person2()
a2.add1()

'''

#os module:
'''
import os
print(os.path.abspath(__file__))
os.mkdir("New")
print(os.getcwd())
os.chdir('D:\\students')
print(os.getcwd())
print(os.listdir())
os.rename("sample.txt","student.txt")
print(os.path.exists('D:\\students'))
'''

#file handling:
'''
import os
    #open(),read(),write(),close()
#creating a new file:

f=open('samplefile.txt','x')
f.close()
#write a Particular file:
f=open("samplefile.txt",'w')
f.write("Hello World")
f.close()
f.open("samplafile.txt",'r')
print(f.read())
#update file:
f=open("samplefile.txt",'a')
f.write("Hello World")
f.close()

with open("samplefile.txt",'a')as f:
    f.write("\nthis is new line")
with open("samplefile.txt",'a')as f:
    print(f.readlines())


'''

#super()
'''
class parent:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class child(parent):
    def __init__(self,id,name,age):
        super().__init__(id,name)
        self.age=age
    def print(self):
        print(self.id)
        print(self.name)
        print(self.age)
c1=child(101,'Raja',20)
c1.print()

'''

#Date Time Module:

import datetime as d
'''
print(d.datetime.now())
print(d.date(2024,10,23))     #yyyy,mm,dd
a=d.date.today()
print(a)
print(a.day)
print(a.month)
print(a.year)
print(a.isoweekday())
b=d.timedelta(days=100)
c=a+b
print(c)
print((c-a).days)
'''
#Time module:
print(d.time(10,50,34))             #hh,mm,ss,optional
a=d.time(10,30,20)
print(a)
print(a.hour)
print(a.minute)
print(a.second)
b=d.datetime.now()
print(b.strftime('%A'))
