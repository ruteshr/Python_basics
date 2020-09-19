#list basics
#list creation
a=[]
b=[1,2,3,4]
c=['a','b','c','d']

#========================INSERTING ELEMENT AT LAST========================#
#inserting one number at last
b=[1,2,3,4]
b.append(5) #output: [1,2,3,4,5]

#Inserting one string at last
c=['a','b','c','d']
c.append('e') #output: ['a','b','c','d','e']

#Inserting one list at last
b=[1,2,3,4]
d=[1,1,1,1,1,1]
c=b+d #output: [1,2,3,4,1,1,1,1,1,1]
#Inserting one list at last using extend() method
a=['a','b','c','d']
b=['ragul','ragavendra']
a.extend(b) 
print(a)#['a','b','c','d','ragul','ragavendra']


#========================INSERTING ELEMENT BASED ON INDEX ========================#
#Inserting one number based on index
b=[1,2,3,4]
b.insert(3,10) #output: [1,2,3,10,4]

#Inserting one string based on index
c=['a','b','c','d']
c.insert(3,'m') #output: ['a', 'b', 'c', 'm', 'd']

#Inserting one list to another based on index
a=['a','b','c','d']
b=['xq','dy','z']
pos=2 #inserting at 2nd position
a[pos:pos]=b 
print(a)#output: ['a','b','xq','dy','z','c','d']
'''or'''
a=['a','b','c','d']
b=['xq','dy','z']
for i in b:
    a.append(i)
print(a
      
#========================ADDING TWO LIST ELEMENT BY ELEMENT========================#
a=[1,2,3]
b=[1,1,1,1]
c=[]
for i,j in zip(a,b):
    c.append(i+j)
print(c)#Output: [2,3,4]

#========================SPLITTING WORD TO LIST ========================#
a='ragul'
b=[]
b.extend(a)
print(b)#output: ['r','a','g','u','l']

#========================DELETING BASED ON SPECIFIED INDEX========================#
#del method removes the specified index
a=['a','b','c','d']
del a[1:3]
print(a)#output: ['a','d']

#deleting the whole list
a=['a','b','c','d']
del a
print(a)#output: 'a' is not found

#clearing the whole list
a=['a','b','c','d']
a.clear()
print(a)#output: [] getting empty list

#pop() method will print the deleted element
a=['a','b','c','d']
a.pop(2)#it will print c
print(a)#output: ['a','b','d']

#========================REMOVING BASED ON SPECIFIED INDEX========================#
a=['a','b','c','d']
a.romove('c')
print(a)#output ['a','b','d']

#========================GETTING INPUT AS LIST========================#
#get the STRING,split by space and store it into the list
a=input().split()
#input: ra gul ra ga
print(a)#output: ['ra','gul','ra','ga']
 
#get the number, split by space and store it into the list
a=lsit(map(int,input().split())) # map method is used to do certain function(here int) for all the sequence, map will return iteration so we are using list
#Input: 43 56 32 3
print(a)#Output: [43,56,32,3]

#========================JOINING THE LIST========================#
#joining the numbers without space
a = [1, 2, 3]
s=[str(x) for x in a]
s="".join(s)
print(s)#output: 123
'''OR'''
a=[1,2,3]
for x in a:
    print(x,end="")

#joining  the string Without space
a=['a','b','cy']
b="".join(a)
print(b)#Output: abcy

#With space
a=['ragul','ragavedra','B']
b=" ".join(a)
print(b)#Output: ragul ragavendra B

#========================CHANGING THE VALUE IN THE LIST========================#
#changing the number
a=[1,2,4,5]
a[2]=3
print(a)#output: [1,2,3,5]

#changing the string
a=['apple','mango','pomo']
a[1]='jackfruit'
print(a)#output: ['apple','jackfruit','pomo']

#========================COPYTING THE LIST========================#
a=['a','b','c']
b=list(a)
print(b)#Output: ['a','b','c']

#========================SORTING THE LIST========================#
#Sorting numbers
a=[3,4,2,5,1]
a.sort()
print(a)#Output: [1,2,3,4,5]
a.sort(reverse=True)
print(a)#Output: [5,4,3,2,1]

#Sorting alphabets
a=['yum','alpha','tom','azure']
a.sort()
print(a)#Output: ['alpha', 'azure', 'tom', 'yum']
a.sort(reverse=True)
print(a)#Output: ['yum', 'tom', 'azure', 'alpha']

#Sorting based on the length of the value 
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)#Output: ['VW', 'BMW', 'Ford', 'Mitsubishi']
cars.sort(key=myFunc,reverse=True)
print(cars)#Output: ['Mitsubishi', 'Ford', 'BMW', 'VW']

#========================SET()========================#
#set numbers
a=[1, 2, 4, 3, 2, 5, 6, 5, 7, 3, 8, 9]
b=set(a)
print(b)#Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(list(b))# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9] to get in list

#set words
a=['ragul','B','ragavendra','B','ragul']
b=set(a)
print(b)#Output: {'ragul', 'B', 'ragavendra'}
print(lsit(b))#Output: ['ragul', 'B', 'ragavendra']


