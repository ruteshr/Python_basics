class person:
    def greetings(self):#self is an argument to get an object like p1 p2
        print("Hi! How are you?")
p1=person()#--> Creating Object(p1) for person like this we can create multiple object
p2=person()
p1.greetings()#--> Object itself calling the function Here we are passing p1 as an argument
p2.greetings()
#OUTPUT:
#Hi! How are you?
#Hi! How are you?
#===============================__init__ METHOD=======================================
'''This method is used to initialize a variable and it was called automatically after creating an object '''
class person:
    def __init__(self):
        print("Good morning")
    def greetings(self):
        print("Hi! How are you?")

p1=person()
p2=person()
p1.greetings()
p2.greetings()
#OUTPUT:
#Good morning -->After creating an object p1 the __init__ method was called automatically 
#Good morning --> for p2

#Hi! How are you? 
#Hi! How are you?
#===============================PASSING ARGUMENT=======================================
class person:
    def __init__(self, name, age):
        #initializing the variable
        self.n=name
        self.a=age
    def greetings(self):
        print("Hi! {} Your age is {}".format(self.n,self.a))#n and a are not local variable it belongs to an object, so we are using as self.n and self.a

p1=person('Ramu',20)
p2=person('Gopal',40)
p1.greetings()
p2.greetings()
#OUTPUT:
#Hi! Ramu Your age is 20
#Hi! Gopal Your age is 40
#====================CONSTRUCTOR, SELF AND COMPARING OBJECT==========================
#Every time you allocated an object it creates a new space in an heap memory
class person:
    pass #this is an empty class
p1=person()
p2=person()
print(id(p1))#this will print the address of an object
print(id(p2))
#OUTPUT:
#2202666198600
#2202666077896
#Note:
''' The size of an object is depends on the number of variable and size of each variable'''
#==========================CHANGING THE VALUE==============================
class person:
    def __init__(self):
        self.name="Ramu"
        self.age=20
p1=person()
p2=person()

#Here both the object has same value(i.e same name and age)
print(p1.name)#OUTPUT: Ramu
print(p2.name)#OUTPUT: Ramu

#if we need the change the value of any object(eg. p2)
p2.name="Gopal"
p1.age=12
print(p1.name, p1.age)#OUTPUT: Ramu 12
print(p2.name, p2.age)#OUTPUT: Gopal 20

#=====================COMPARING TWO OBJECT===========================
class person:
    def __init__(self):
        self.name="Ramu"
        self.age=20
    #creating a function two compare the object
    def compare(self,other):#these are two object
        if(self.age== other.age):
            return True
        else:
            return False
p1=person()
p2=person()
p1.age=12
#if we need to compare the age of two person
if(p1.compare(p2)):#p1--> self   #p2-->other
    print("They are same age")
else:
    print("They are diff age")
#OUTPUT:
#They are diff age

#=================CLASS(STATIC) and INSTANCE VARIABLE====================
#******INSTANCE******
''' The instance variable are different for different object. if we change the value
    one object it won't affect the other object.
'''
class car:
    def __init__(self):
        self.company='BMW'#\ These are called instance variable or instance namespace
        self.mileage=15   #/ OR the variable inside the __init__ are called instance variable
c1=car()
c2=car()
c1.mileage=20 #If we change the value of c1 mileage it won't affect the other object(c2)
print(c1.company,c1.mileage)
print(c2.company,c2.mileage)
#OUTPUT:
#BMW 20
#BMW 15

#******CLASS/STATIC VARIABLE******
'''
The static variable are same for all the object if we change the value of static variable
it will affect all the object.
'''
class car:
    wheel=4      #\These are called Class/Static variable
    fuel='petrol'#/the variable outside the __init__ method but inside the class are called static/class variable
    def __init__(self):
        self.company='BMW'
        self.mileage=15
c1=car()
c2=car()

car.wheel =5#if we change the class variable it will affect all the object
print(c1.company,c1.mileage,c1.wheel)
print(c2.company,c2.mileage,c2.wheel)
#OUTPUT:
#BMW 15 5
#BMW 15 5

#=====================METHODS IN PYTHON=================
#******INSTANCE METHOD******
'''The method which is working on the instance variable is called instance method'''
class student:
    def __init__(self,name,discipline):#--> This is called instance method 
        self.nam=name
        self.dis=discipline
s1=student('Ravi', 'ECE')
s2=student('Gopal','CSE')
print(s1.nam,s1.dis)
print(s2.nam,s2.dis)
#OUTPUT:
#Ravi ECE
#Gopal CSE

#******CLASS METHOD******
'''The method which is working on the class variable is called class method
and we need to use special decotator @classmethod'''

class student:
    school='ABC'#--> class variable
    def __init__(self,name,discipline): 
        self.nam=name
        self.dis=discipline
        
    @classmethod #special decotator
    def getschool(cls):#-->This is call class method because it uses class variable
        return cls.school
    
s1=student('Ravi', 'ECE')
s2=student('Gopal','CSE')
print(s1.nam,s1.dis)
print(s2.nam,s2.dis)

print(student.getschool())

#OUTPUT:
#Ravi ECE
#Gopal CSE
#ABC

#******STATIC METHOD******
'''The method which is not working on both class and instance variable is called static mehtod
and we need to use special decotator @staticmethod'''


class student:
    school='ABC'
    def __init__(self,name,discipline): 
        self.nam=name
        self.dis=discipline
        
    @classmethod 
    def getschool(cls):
        return cls.school

    @staticmethod #special decotator
    def info():#no need to receive any object because this is static method. we can receive any argument
               #to perform action(eg. to do a fibinocci series because it doesn't depend on class/instance variable)
               #but it shouldn't be a class or instance variable
        return("This is the student list of....ABC school")
               
s1=student('Ravi', 'ECE')
s2=student('Gopal','CSE')
print(s1.nam,s1.dis)
print(s2.nam,s2.dis)
print(student.getschool())

print(student.info())#no need to pass any object but we can pass argument

#OUTPUT:
#Ravi ECE
#Gopal CSE
#ABC
#This is the student list of....ABC school

