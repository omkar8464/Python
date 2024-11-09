'''#if-elif-else(SYNTAX)
if(condition):
    statement 1
elif(condition):
    statement 2
else:
    statement n

'''
#Traffic Light Code
light=input("Light:")
if(light=="red"):
    print("Stop")
elif(light=="green"):
    print("Go")
elif(light=="yellow"):
    print("Wait")
else:
    print("Light is not Working")

#If-elif-else
marks=int(input("Enter the marks:"))
if marks>=95:
    grade="A"
elif marks>=80 and marks<90:
    grade="B"
elif marks>=70 and marks<80:
    grade="C"
else:
    grade="D"
print(grade)

'''#If-else
age=16
if age>=18:
    print("Person can Vote")
else:
    print("Person can not vote")

#Nested-if
marks=85    #78/95
if marks>=80:
    print("you will get a new phone")
    if marks>=90:
        print("you can go to a trip")
else:
    print("No phone allow for a month")



#if-elif-else problem
A=int(input("Enter the number:"))
G=input("Enter Gender:")
if(A==1 or A==2) and (G=="M"):
    print("fees is 100")
elif((A==3 or A==4) or G=="F"):
    print("fees is 200")
elif(A==5 and G=="M"):
    print("fees is 300")
else:
    print("Not Deposited")
    

food=input("")
print("eat") if food=="cake" or food=="jelabi" else print("not")


#Calculate simple interest
p=int(input("Enter the principle amount:"))
r=int(input("Enter the rate:"))
t=int(input("Enter the time:"))
si=(p*r*t)/100
print(si)

'''