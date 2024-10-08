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
