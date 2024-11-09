#Creating a class
'''class Student:
    name="Omkar"

#creation of object(object is also known as instance)
s1=Student()
print(s1.name)
s2=Student()
print(s2.name)'''

'''
class Car:
    color="Blue"
    brand="BMW"
car1=Car()
print(car1.color)
print(car1.brand)'''


'''
class Student:
    #agar hm constructor nhi bana rahe h to by default python bana dega
    #default constuctor---
    #def __init__(self):
    #    pass
    
    #parameterize constructor means self ke alawa kuch aur bhi parameter atte hai
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

#creation of object(object is also known as instance)
s1=Student("Omkar", 95)
print(s1.name,s1.marks)
s2=Student("ram", 87)
print(s2.name,s2.marks)
'''

'''
#Method in OPPs
class Student:
    college_name="NIET"#class attribute
    def __init__(self,name,marks):#constructor
        self.name=name
        self.marks=marks
    def hello(self):#method
        print("hello",self.name,self.marks)
    def get_marks(self):
        return self.marks
s1=Student("Omkar",87)
s1.hello()
print(s1.get_marks())
print(Student.college_name)
'''

'''
#Create student class that takes name and marks of 3 subject as argument in constructor.
#Then create a method to print the average.
class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def display_name(self):
        print("My name is:",self.name)
    def avg(self):
        average=(self.marks1+self.marks2+self.marks3)/3
        print("Average marks of 3 subject",average)

s1=Student("Omkar",90,80,70)
s1.display_name()
s1.avg()


#Static method
class Student:
    def __init__(self,name):#constructor
        self.name=name
    def hello(self):#method
        print("hello",self.name)

    #Static method
    @staticmethod
    def college():
        print("NIET")

s1=Student("Omkar")
s1.hello()
s1.college()
'''

'''
#Abstraction
#Create Account class with 2 attributes - balance and account no.
#Create method for debit,credit and printing the balance
class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("Total balance =",self.get_balance())

    #Credit method
    def credit(self,amount1):
        self.balance+=amount1
        print("Rs.",amount1,"was credited")
        print("Total balance =",self.get_balance())

    def get_balance(self):
        return self.balance


acc1=Account(10000,220133153)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(50000)
acc1.debit(20000)
'''
'''
#del keyword
class Student:
    def __init__(self,name):
        self.name=name

s1=Student("Omkar")
print(s1.name)
del s1.name
print(s1.name)
'''

'''
#Public access modifier
# program to illustrate public access modifier in a class
class Geek:
    def __init__(self, name, age):
        # public data members
        self.geekName = name
        self.geekAge = age
    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.geekAge)

# creating object of the class
obj = Geek("R2J", 20)
# finding all the fields and methods which are present inside obj
print("List of fields and methods inside obj:", dir(obj))
# accessing public data member
print("Name:", obj.geekName)
# calling public member function of the class
obj.displayAge()
'''

'''
#Private
class Person:
    __name="anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1=Person()
#print(p1.__name)#error throw karega
#print(p1.__hello())#error throw karega
print(p1.welcome())
'''
'''
#Inheritance
#Example of single Inheritance
class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Fortuner")
car2=ToyotaCar("prius")
print(car1.name)
print(car1.start())

#Multi-level Inheritance
# Python program to demonstrate
# multilevel inheritance

# Base class
class Grandfather:
	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername
		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname
		# invoking constructor of Father class
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)

# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
'''

'''
#Multiple Inheritance
# Python program to demonstrate
# multiple inheritance

# Base class1
class Mother:
    def __init__(self, mother):
        self.mother = mother

class Father:
    def __init__(self, father):
        self.father = father

class Child(Mother, Father):
    def __init__(self, child, mother, father):
        self.child = child
        # invoking constructor of Mother,Father class
        Mother.__init__(self, mother)  # Initialize the Mother class
        Father.__init__(self, father)  # Initialize the Father class
        

    def print_name(self):
        print('Mother name:', self.mother)
        print("Father name:", self.father)
        print("Child name:", self.child)

# Create an instance of Child
ch1 = Child("Lucky","Sita","Ramlal")
print(ch1.mother)# Access mother's name directly
ch1.print_name()  # Print all names


#Super() method
# A Python program to demonstrate inheritance
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)
class Emp(Person):
    def __init__(self, name, id):
        self.name_ = name
        #super method means to call the parent class
        super().__init__(name, id)

    def Print(self):
        print("Emp class called")

Emp_details = Emp("Mayank", 103)
# calling parent class function
print(Emp_details.name_, Emp_details.id)
'''

'''
#class method
#Agar hm hm chate hai ke class ke ander jo name h wo change ho jaye to
class Person:
	name="anonymous"
	#def changeName(self,name):
		#self.name ke jagha class.name likhte hai
		#Person.name=name
		#self.__class__.name="rahul"
		#Person.name=name
	@classmethod
	def changeName(cls,name):
		cls.name=name#ye directlty change kar dega class mei

	
p1=Person()
p1.changeName("omkar")
print(p1.name)
print(Person.name)
'''

'''
#Property decotator
class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    #def clacPercentage(self):
    #    self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"

std1=Student(98,97,99)
print(std1.percentage)
std1.phy=86
print(std1.percentage)
'''

'''
#Polymorphism
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)
    
num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

num3=num1+num2
num3.showNumber()

num4=num2-num1
num4.showNumber()
'''

#1.Create a Circle class to create a circle with radius r using the constructor.
#Define an Area() method of the class which calculate the area of the circle.
#Define a Perimeter() method of the class which allow you to calculate the perimeter of the circle.
'''class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius

c1=Circle(21)
print(c1.area())
print(c1.perimeter())
'''
#2.Define a Employee class with attributes role, department and salary.
#This class also showDetails() method.
#Create an Engineer class that inherits properties from Employee and has additional attributes:nameand age
'''class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("Role =",self.role)
        print("Department =",self.dept)
        print("Salary =",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","750000")

engg1=Engineer("Omkar",22)
engg1.showDetails()
'''

#3.Create a class called Order which stores item and price.
#Use Dunder function __gt__() to convey that:
#order1>order2 if price of order1>price of order2
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price>odr2.price

odr1=Order("chips",20)
odr2=Order("tea",15)
print(odr1>odr2)