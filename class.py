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

class student:
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
nandha.put()
        
