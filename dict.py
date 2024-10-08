# creating a dict
d={'reg_no':140,'name':"raja",'age':20}
print(d['name'])
    #key    #value
'''print(d)

#accessing value from dictionary(dict)
print(d['reg_no'])  #cannot access by index .only access by key value

print(d.items())    #it brings all the items
print(d.keys())     #it brings only keys
print(d.values())   #it brings only values


#adding or updating dictionary:

d['city']='madurai'
print(d)'''

#update function:

'''d.update({'reg_no':155}) #we can update only one key values
#print(d)

c={'qualification':'b.com'} #we can update more than one key values
d.update(c)
print(d)'''

#delete

    #pop()  use key to delete
    #del
    #clear()

#d.popitem()     #it delete last key:values
#d.pop('name')
#print(d)
#d.clear()
#del d
#del d['name']
#print(d)


    #using for loop
'''for i in d:
    print(i)''' #default is key 

'''for i in d:
    print(d[i])     #to get value'''

'''for i in d.items():    #you can use d.value(),d.keys(),d.items() to get direct element
    print(i)'''

'''for i in d.items():
    x,y=i           #it assign key =x,values =y 
    print(x,y)'''

    #copy()
'''a=d.copy()
print(a)'''

    #get()
'''a=d.get("age")
print(a)'''

    #setdefault()
'''b=d.setdefault('city','madurai')
print(d)'''

    #fromkeys()
'''x=('address','state')
y='tamilnadu'
z=d.fromkeys(x,y)
print(z)'''

    #add key:values in dynamic method

'''a=input("Enter the keys :")
b=input("Enter the values :")
#first method
d[a]=b
print(d)
#second method
c={a:b}
d.update(c)
print(d)'''

    #nested dictionary
#a={'key':{'key':'value'}}
'''
a={'a1':{'Name':'raja','age':20,'city':'Madurai'},
   'a2':{'Name':'ragu','age':21,'city':'Madurai'},
   'a3':{'Name':'ravi','age':22,'city':'Madurai'}
   }
'''
#print(a['a1']['Name'])


#accessing values in dictionary
#task

'''
for i,b in a.items():
    print(i)
    for j in b:
        print(j,':',b[j])

'''
'''for i in a.items():
    x,y=i
    print(x)
    for j in y:
        print(j,':',y[j])'''


#z=int(input("enter the pair :"))
a={}
#1
'''for i in range(z):
    x=input("enter the keys :")
    y=input("enter the values :")
    a[x]=y
print(a)'''

#2

'''for i in range(50):
    x=input("enter the key :")
    if x=="ok":
        break
    y=input("enter the values :")
    a[x]=y
print(a)'''

#3

'''for i in range(50):
    z=input("enter the key :")
    
    if z=='ok':
        break
    x=input("enter the name :")
    y=input("enter the city :")
    w=input("enter the age :")
    
   
    a.update({z:{'name':x,'city':y,'age':w}})
   
print(a)'''

#4

'''for i in range(50):
    z=input("enter the key :")
    if z=='ok':
        break
    x=input("enter the product name :")
    y=input("enter the id :")
    w=input("enter the price :")
    b=input("enter the expiry :")
    a[z]={
        'product':x,
        'id':y,
        'price':w,
        'expiry':b
        }
print(a)'''

#5
d={}
l=['name','age','city']
z=int(input("enter the number of person :"))
for i in range(z):
    x=input("enter the key :")
    y={}
    for j in l:
        y[j]=input(j)
        
    d[x]=y
print(d)
  



    



