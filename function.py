    #function
#syntax
'''
def function_name(parameter/argument):
    function block start


    function block end
print()
'''

#example for function

#1
'''def print1():
    a='Hello Friends'
    print(a)
print1()        #it will call on refresh the page
print('End of the program')'''

#2

'''a=int(input('Enter the value1 :'))
b=int(input('Enter the value2 :'))
c=input('\n1.Add\n2.subract\n3.multiply\n4.division\n5.modulo\n\n\t\tchoose any one~')

def add():
    print(a+b)
def sub():
    print(a-b)
def multi():
    print(a*b)
def div():
    print(a/b)
def m_div():
    print(a%b)

    
if c=='+':
    add()
elif c=='-':
    sub()
elif c=='*':
    multi()
elif c=='/':
    div()
elif c=='%':
    m_div()
else:
    print("invalid")'''
#2,,

'''def calculator():
    a=int(input('Enter the value1 :'))
    b=int(input('Enter the value2 :'))
    c=input('\n1.Add\n2.subract\n3.multiply\n4.division\n5.modulo\n\n\t\tchoose any one~')

    def add():
        print(a+b)
    def sub():
        print(a-b)
    def multi():
        print(a*b)
    def div():
        print(a/b)
    def m_div():
        print(a%b)
    if c=='+':
        add()
    elif c=='-':
        sub()
    elif c=='*':
        multi()
    elif c=='/':
        div()
    elif c=='%':
        m_div()
    else:
        print("invalid")
calculator()
d=input("do you want one more time")
if d=="yes":
    calculator()
else:
    print("thankyou")'''
    
#3

def calculator():
    a=int(input('Enter the value1 :'))
    b=int(input('Enter the value2 :'))
    c=input('\n1.Add\n2.subract\n3.multiply\n4.division\n5.modulo\n\n\t\tchoose any one~')
    process(a,b,c)

def process(a,b,c):
     def add():
        print(a+b)
     def sub():
        print(a-b)
     def multi():
        print(a*b)
     def div():
        print(a/b)
     def m_div():
        print(a%b)
     if c=='+':
        add()
     elif c=='-':
        sub()
     elif c=='*':
        multi()
     elif c=='/':
        div()
     elif c=='%':
        m_div()
     else:
        print("invalid")


calculator()

    



