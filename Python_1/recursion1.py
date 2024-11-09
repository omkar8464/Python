#recursive function
#Natural number in reverse order
def show(n):
    if(n==0):#kaha pe ja ke stop hoga
        return
    print(n)
    show(n-1)
show(5)

#Factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#Write a recursive function to calculate the sum of first n natural numbers.
def show(n):
    if(n==0):#kaha pe ja ke stop hoga
        return 0
    return show(n-1)+n
sum=show(5)
print(sum)

#Write a recursive function to print all element in a list.
#use list&index as parameter
def print_list(lst,idx=0):
    if(idx==len(lst)):
        return
    print(lst[idx])
    print_list(lst,idx+1)

fruits=["mango","banana","apple","gauva"]
print_list(fruits)