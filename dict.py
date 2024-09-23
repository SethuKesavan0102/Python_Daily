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

d.update({'reg_no':155}) #we can update only one key values
#print(d)

c={'qualification':'b.com'} #we can update more than one key values
d.update(c)
print(d)

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
