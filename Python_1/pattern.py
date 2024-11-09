
#solid rectangle
'''
*****
*****
*****
*****


n=5
for i in range(n):   #outer loop for columns
    for j in range(n):   #inner loop for rows
        print("*",end=" ")
    print()

'''


#Hollow Rectangle
'''
* * * * *
*       *
*       *
* * * * *

n=4
m=5
for i in range(n):
    for j in range(m):
        if(i == 0 or j == 0 or i == n-1 or j == m-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''

#Half Pyramid
'''
*
* *
* * *
* * * *
* * * * *

n=5
for i in range(n):  #outer loop
    for j in range(i+1):  #inner loop
        print("*",end=" ")
    print()


* * * * *
  * * * *
    * * *
      * *
        *
n=5
for i in range(n):  #outer loop
    for j in range(i+1):  #inner loop   first increasing triangle
        print("",end=" ")
    for j in range(i,n):  #inner loop   decreasing triangle
        print("*",end="")
    print()

'''

#reverse triangle
'''
* * * * *
* * * *
* * *
* *
*

n=5
for i in range(n):  #outer loop
    for j in range(i,n):  #inner loop
        print("*",end=" ")
    print()
'''

#Right sided Triangle
'''
_ _ _ _ *
_ _ _ * *
_ _ * * *
_ * * * *
* * * * *

n=5
for i in range(n):  #outer loop
    for j in range(i,n):  #inner loop
        print("",end=" ")   #these line show the space on the left side
    for j in range(i+1):  #inner loop
        print("*",end="")

    print()
'''


#Pyramid Pattern
'''
    *
   ***
  *****
 *******
*********
'''

n=5
for i in range(n):  #outer loop
    for j in range(i,n):  #inner loop
        print("",end=" ")   #these line show the space on the left side
    for j in range(i):  #inner loop
        print("*",end="")
    for j in range(i+1):  #inner loop
        print("*",end="")
    print()



"""
1
1 2
1 2  3
1 2 3 4
1 2 3 4 5  """

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()