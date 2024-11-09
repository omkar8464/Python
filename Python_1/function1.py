'''def calc_sum(a,b):
    s=a+b
    print(s)
    return s
calc_sum(2,3)
calc_sum(9,1)


def sum(a,b):
    s=a+b
    return s
cal=sum(4,5)
print(cal)

#Print average of 3 number.
def cal_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    return avg
total_avg=cal_avg(5,5,5)
print(total_avg)


#Built-in Function
#1.print()
#2.len()
#3.type()
#4.range()

#Default parameter
def cal_mul(a,b=2):
    return a*b
product=cal_mul(1)
print(product)

'''
'''*lst Python mein unpacking operator hota hai jo kisi list
(ya aur iterable, jaise tuple) ke elements ko individual values mein unpack karta hai.
Jab print() function ke saath *lst use karte hain, toh yeh list ke har element ko space ke saath alag-alag print kar deta hai bina kisi loop ke.'''
#1.Write a function to print the length of a list.(list is the parameter)
cities=["delhi","up","noida","gkp","lkn"]
def print_len(list):
    print(len(list))
print_len(cities)
#2.Write a function to print the element of a list in a single line.(list is the parameter)
#print(xyz[0],end=" ")single line mei print hoga
def print_list_in_single_line(lst):
    print(*lst,end=" ")

my_list=[1,2,3,4,5]
print_list_in_single_line(my_list)
#Another method
cities=["delhi","up","noida","gkp","lkn"]
def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)
print()

#Write a function to find the factorial of n.(n is the parameter)
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

factorial(5)


#Write to convert USD to INR
# 1USD=83
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val, "USD =", inr_val, "INR")
converter(2)

# Waf to take input from the user of a number and if its odd print "odd" and if it is even print "even"
n=int(input("Enter the number:-"))
def fun(n):
    if (n%2==0):
        print("Even")
    else:
        print("Odd")
fun(n)