def cust():
    customer=["loki","nandha","sk","ela","arjun"]
    amount=(20000,15000,10000,30000,4500)


    sender=input("Enter the sender name : ")
    receiver=input("Enter the receiver name : ")
    transfer=int(input("Enter the transfer amount : "))
    send(customer,amount,sender,receiver,transfer)


def send(customer,amount,sender,receiver,transfer):
    for i in customer:
        if(i==sender):
            x=(customer.index(i))
            print("the",sender,"balance",amount[x])
            y = amount[x] - transfer
            print("The",sender,"Current balance is", y)
            break
    
    for j in customer:
        if(j==receiver):
            x=(customer.index(j))
            z = amount[x] + transfer
            print("The",receiver,"current amount is", z)
            break
cust()
 
