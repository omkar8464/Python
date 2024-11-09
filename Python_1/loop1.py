#For loop
#Loop are used for sequential traversal.For traversing list,tuple,string etc.
'''list1=[1,2,3,4]
for i in list1:
    print(i)

str="omkarsingh"
for char in str:
    print(char)


for i in range(1,6):
    print(i)

#gap
for i in range(1,6,2):
    print(i)

#String
for i in range(1,6):
    print("om")

#Any Table
n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)


#Print the element of the following list using a loop.
#[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
for i in nums:
    print(i)

#Search for a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
x=49
index=0
for i in nums:
    if(i==x):
        print("found at index",index)
    index +=1


#Range()
#Print the number from 1 to 100
for i in range(1,101):
    print(i)


#Print the number from 100 to 1.
for i in range(100,0,-1):
    print(i)

n=int(input("Enter the number"))
a=1
for i in range(1,11):
    print(n,"x",a,"=",n*a)
    a=a+1

#even number
for i in range(0,100,2):
    print(i)

#odd number
list1=[]
for i in range(1,100,2):#print in the form of list
    list1.append(i)
print(list1)
'''

#WAP to find the sum of first n numbers
n=int(input("Enter the number:-"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("The sum is",sum)

#WAP to find the factorial of first n numbers
n=int(input("Enter the number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#pass statement
#for i in range(10):
    #empty leave karna hai
#    pass
#print("start from here...")
