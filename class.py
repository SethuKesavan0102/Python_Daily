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
