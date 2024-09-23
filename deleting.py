a=[20,30,35,40,30,10,20,20,20,20,20,20]
'''b=int(input("Enter the searching value"))
c=int(input("Enter the deleting value"))
d=0
    # to delete the value
for i in a:
    if i==b:
        d=1
        
if d==1:
    x=a.index(c)
    del a[x]
    print("the crt value",a)
else:
    print("value not found")'''

        #to remove a duplicate value

'''for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]==a[i]:
            a.pop(j)
            break
print(a)'''


for i in a:
    for j in a:
        if i==j and a.count(i)>1:
            a.remove(i)
            print(a)


 
    
        
  


   
