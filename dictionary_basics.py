#==========INSERT DATA IN DICTIONARY==========#
#Inserting one by one
a={}
a['Name']='Ragul'
a['Age']=20
a['Gender']='Male'
print(a)#OUTPUT: {'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}

#Inserting Directly
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
print(a)#OUTPUT: {'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}

#Getting Input (one dictonary)
def detail():
    a={}
    a['Name']=input('Enter Name')
    a['Age']=int(input('Age'))
    a['Gender']=input('Gender')
    return a
temp=detail()#INPUT: Ragul \n 20 \n Male
print(temp)#OUTPUT: {'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}

#Getting Input (Multiple Dictonary)
def detail():
    a={}
    a['Name']=input('Enter Name')
    a['Age']=int(input('Age'))
    a['Gender']=input('Gender')
    return a
n=int(input("Enter no of Dictionary"))
b={}
#to get multiple input
for i in range(n):
    b[i]=detail()
#to print the whole dic
print(b)
#OUTPUT:
'''
{0: {'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}, 
 1: {'Name': 'Ragavendra', 'Age': 20, 'Gender': 'Male'}}
'''
#to print only name
for i in range(n):
    print('{}\t{}'.format(b[i]['Name'],b[i]['Age']))
#OUTPUT
'''
Ragul		20
Ragavendra	    20
'''
#===========COPYING THE DICTIONARY USING dict() function==========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
b=dict(a)
print(b) #OUTPUT: {'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}

#===========FINDING THE LENGTH OF THE DICTIONARY===========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
print(len(a)) # OUTPUT: 3

#==========DELETING THE DICTIONARY==========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
del a['Age']#enter key value which you want to delete
print(a)#OUTPUT: {'Name': 'Ragul', 'Gender': 'Male'}

#==========ACCESSING VALUE BY KEY==========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
print(a['Age'])#OUTPUT: 20
#OR
print(a.get('Age'))#OUTPUT: 20

#==========ACCESSING KEY BY VALUE==========#
def get_key(val):
    for key,value in a.items():
        if(value==val):
            return key
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
print(get_key('Male'))#OUTPUT: Gender
print(get_key(20))#OUTPUT: Age

#==========PRINTING ONLY THE KEY ==========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
print(a.keys())#OUTPUT: dict_keys(['Name', 'Age', 'Gender'])
#to print key as list
print(list(a.keys()))#OUTPUT: ['Name', 'Age', 'Gender']

#==========PRINTING ONLY THE VALUE==========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
print(a.values())#OUTPUT: dict_values(['Ragul', 20, 'Male'])
#to print value as list
print(list(a.values()))#OUTPUT: ['Ragul', 20, 'Male']

#===========PRINTING KEY ONE BY ONE==========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
for x in a:
    print(x)
#OUTPUT:
#Name
#Gender
#Age
#==========PRINTING VALUE ONE BY ONE=========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
for x in a:
    print(a[x])
#OUTPUT:
#Ragul
#Male
#20

#==========PRINTING KEY AND VALUE ONE BY ONE==========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
for x,y in a.items():
    print(x,y)
#OUTPUT:
#Gender Male
#Name Ragul
#Age 20

#==========ADDING ELEMENT==========#
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
a["year"]=2000
print(a)#OUTPUT: {'Gender': 'Male', 'Name': 'Ragul', 'Age': 20, 'year': 2000}

#==========REMOVING AN ITEM=========#
#pop() method removes the item with the specified key name: 
a={'Name': 'Ragul', 'Age': 20, 'Gender': 'Male'}
a.pop('Age')#OUTPUT: 20
print(a)#OUTPUT: {'Name': 'Ragul', 'Gender': 'Male'}

