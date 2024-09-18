customer=["loki","nandha","sk","ela","arjun"]
amount=[20000,15000,10000,30000,4500]
j=0
b=0
a=0

sender=input("Enter the sender name : ")
receiver=input("Enter the receiver name : ")
transfer=int(input("Enter the transfer amount : "))

'''for i in customer:
    if i==sender:
        amt=amount[j]
        print("Available amount : ",amt)
        x=amt - transfer
        print("available current balance : ",x)
    j+=1

for i in customer:
    if i==receiver:
        amt=amount[b]
        print("The",receiver,"available amt",amt)
        y=amt + transfer
        print("The",receiver,"current balance ",y)
    b+=1'''




for i in customer:
    if i==sender or i==receiver:
        a=1
        break
else:
    print("the sender or receiver is not availabe")
        
for i in customer:
    if a==1:
        if i==sender:
            amt=amount[j]
            print("Available amount : ",amt)
            x=amt - transfer
            print("available current balance : ",x)
        j+=1
        
    
for i in customer:
    if a==1:
        if i==receiver:
            amt=amount[b]
            print("The",receiver,"available amt",amt)
            y=amt + transfer
            print("The",receiver,"current balance ",y)
        b+=1
        
        

    
