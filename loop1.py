customer=["sk","arjun","loki","siva","karthi"]
amount=[10000,35000,22000,5000,2000]

sender=input("Enter sender name :")
receiver=input("Enter receiver name :")
sendamt=int(input("Enter the transfer amount :"))

for i in customer:
    if(i==sender):
        x=(customer.index(i))
        print("the",sender,"balance",amount[x])
        y = amount[x] - sendamt
        print("The",sender,"Current balance is", y)
        break
    else:
        print("Sender is not available")

for j in customer:
    if(j==receiver):
        x=(customer.index(j))
        z = amount[x] + sendamt
        print("The",receiver,"current amount is", z)
        break
   
        
