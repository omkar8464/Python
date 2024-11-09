#While loop
n=0
while(n<=5):
    print(n)
    n=n+1

#Print numbers from 1 to 100.
"""n=1
while n<=100:
    print(n)
    n=n+1

##Print numbers from 100 to 1.
n=100
while n>=1:
    print(n)
    n=n-1
    

#Print the multiplication table of a number n.
i=1
n=int(input("Enter the number:-"))
while i<=10:
    print(n,"x",i,"=",n*i)
    i=i+1
"""
#Print the element of the following list using a loop.
#[1,4,9,16,25,36,49,64,81,100]

list1=[1,4,9,16,25,36,49,64,81,100]
index=0
while index<len(list1):
    print(list1[index])
    index +=1

#Search for a number x in this tuple using loop.
#(1,4,9,16,25,36,49,64,81,100)
list1=[1,4,9,16,25,36,49,64,81,100]
x=25
index=0
while index<len(list1):
    if(list1[index]==x):
        print("found at idx",index)
        break
    else:
        print("not found")
    index +=1
    

#WAP to find the sum of first n natural numbers
sum=0
n=int(input("Enter the number:-"))
i=1
while i<=n:
    sum=sum+i
    i +=1
print("Total sum",sum)


#WAP to find the factorial of first n numbers
n=int(input("Enter the number"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i +=1
print(fact)