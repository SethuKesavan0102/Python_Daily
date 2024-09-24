# creating a dict
d={'reg_no':140,'name':"raja",'age':20}
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
a={'key':{'key':'value'}}

a={'a1':{'Name':'raja','age':20,'city':'Madurai'},
   'a2':{'Name':'ragu','age':21,'city':'Madurai'},
   'a3':{'Name':'ravi','age':22,'city':'Madurai'}
   }
#print(a['a1']['Name'])


#accessing values in dictionary

'''for i,b in a.items():
    print(i)
    for j in b:
        print(j,':',b[j])'''




for i in a.items():
    x,y=i
    print(x)
    for j in y:
        print(j,':',y[j])


    



