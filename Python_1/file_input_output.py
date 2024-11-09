'''f=open("demo.txt","r")
data=f.read()
#data=f.read(10)#number od element ko bhi print kara sakte hai
f=open("demo.txt","r")
data=f.read()'''

''' Reading a file
1.f.read()  read entire file
2.f.readline()  read one line at a time'''

'''
f=open("demo.txt","r")
data=f.read()
print(data)
#read() funcrion phele he file ko read kar kar le raha h baad mei kuch bacha he nhi th khali space print kara rha hai
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()


f=open("demo.txt","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()

#write()

f=open("demo.txt","w")#write mode
f.write("I want to become a software developer")#overwrite kar dega txt file mei
f.close()

f=open("demo.txt","a")#append means add at last
f.write("\nThen I'll move to USA")
f.close()

f=open("demo.txt","r+")#r+overwrite kar diya hai stating of file mei abc
f.write("abc")
print(f.read())
f.close()


#With Syntax
with open("sample.txt","r") as f:
    data=f.read()
    print(data)
    #f.close likhne ke jarrurt nhi hoti h with automatically close kar deta hai

with open("sample.txt","w") as f:
    f.write("new data")

    

#Deleting a file
import os
os.remove("sample.txt")
'''

#practice question
#Create a new file "practice.txt" using python. add the following data in it.
'''Hi everyone
we are learning File I/OS
using Java
Ilike programming in Java'''
#WAF that replace all occurancees of "java" with "python" in above file
'''with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)
'''
#Search if the word "learning" exists in the file or not
'''word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if word in data:
        print("Found")
    else:
        print("not found")'''

#Write a function in which line of the file does the word "learning" occur first.
#Print -1 if word not found
def find_word_in_file(filename, word):
    with open(filename, "r") as f:
        for line_num, line in enumerate(f, start=1):
            if word in line:
                return line_num
    return -1

# Usage
filename = "practice.txt"
word = "learning"
line_number = find_word_in_file(filename, word)
print(line_number)
