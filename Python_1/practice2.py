#WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
list1=[]
mov=input("Enter 1st movies:")
mov2=input("Enter 2nd movie:")
mov3=input("Enter 3rd movie:")
list1.append(mov)
list1.append(mov2)
list1.append(mov3)
print(list1)

#WAP to check if a list contains a palindrome of element.
#[1,2,3,2,1]    [1,"abc","abc",1]

list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("Palindrome")
else:
    print("Not Palindrome")


#WAP to count the number of students with the "A" grade in the following tuple.
#["C","D","A","A","B","B","A"]

tup=("C","D","A","A","B","B","A")
print(tup.count("A"))

#Store the above value in a list and sort them from"A" to "D".
grade=["C","D","A","A","B","B","A"]
grade.sort()
print(grade)