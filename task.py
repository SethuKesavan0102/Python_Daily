    #task -1
a=[100,20,30,100,40,80,35]
#print(min(a))
#print(max(a))

    # 1st method
    
b=a[0]

for i in a:
    if i < b:
        b=i
print(b)

    #2nd method using nested loop

    
for i in a:
    for j in a:
        if j > i:
            i = j
    
print(i)
    

    
   
