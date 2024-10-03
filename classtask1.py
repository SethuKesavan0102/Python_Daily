print("Welcome to All")
print("Enter your option")

class detail:
    def det(self):
        self.name=""
        self.age=0
        self.rollno=0

    def input(self):
        self.name=input("Enter the name :")
        self.age=int(input("Enter the age :"))
        self.rollno=int(input("Enter the rollno :"))

    def print(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Rollno :",self.rollno)

    def program(self):
        #for i in range(20):
        x=int(input("1.Add Student Details,\n2.View Student Details,\nThe Given Values Must be in a Number :"))

        if x==1:
            self.input()
        elif x==2:
            self.print()
        else:
            print("Wrong")

    def run(self):
        choose=input("Do You Want To Continue (Y/N):")
        if choose=="y":
            self.program()
            self.run()
        else:
            print("Exiting......bye")
        
        
                

            
            

sk=detail()
#ks=detail()
sk.program()
#ks.program()
sk.run()
