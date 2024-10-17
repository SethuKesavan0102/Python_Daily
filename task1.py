#login task:
'''
import datetime as d
username=input("Enter Username :")
password=int(input("Enter Password :"))
class login:
    def __init__(self):
        if username=='sk' and password==1020:
            self.time=d.datetime.now()
            print("Login Successfully")
            self.view()
            
        else:
            print("Login Failed")
        
    

    def view(self):
        print("Do you want to view last login (y/n):")
        self.v=input()
        if self.v=='y':
            #print("Last login :",self.time.strftime('%X'))
            print("Last login :",self.time.hour,":",self.time.minute,":",self.time.second)
        else:
            print("Thank You....")


a1=login()
'''
