'''a=[10,20,30,40]
print(a[2])
print(a[-1])

for i in a:
    print(i)

b=list(x*2 for x in range(1,10))
b[3]=30
print(b)'''

customer=["sk","arjun","loki","siva","karthi"]
amount=[10000,35000,22000,5000,2000]

sender=input("enter sender name :")
receiver=input("enter receiver name :")
sendamt=int(input("enter amount :"))

for i in customer:
   
    if(i==sender):
        x=(customer.index(i))
        print(amount[x])
        y = amount[x] - sendamt
        print("The",sender,"current amount is", y)
        print("sender is available")
        break;
    else:
        print("sender is not availabe")
for j in customer:
    if(j==receiver):
        x=(customer.index(j))
        z = amount[x] + sendamt
        print("The",receiver,"current amount is", z)
        break;
    else:
        print("sender is not availabe")   
    

    

