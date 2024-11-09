'''str="This is a string.\nWe are creating in python."
print(str)

#Concatenation of string
name="Omkar"
surname="Singh"
fullname=name+" "+surname
print(fullname)

#length of string
len1=len(name)
print(len1)
len3=(len(fullname))
print(len3)


#Indexing
str="Welcome to the Python Course"
ch=str[15]
print(ch)
print(str[18])
'''

'''
#Silicing
str="NoidaInstituteofengineeringandtechnology"
print(str[0:10])
ch=str[5:27]
print(ch)
print(str[0:len(str)])
print(str[5:0])

print(str[-26:-1])

'''

#String Function
str="python is a easy language."
#endswith()
print(str.endswith("age."))

#captialize
str=str.capitalize()#sirf first letter ko captial karega
print(str)

#replace
print(str.replace("easy","interpreted"))

#count
print(str.count("a"))

#find
print(str.find("a"))

#islower
print("is".islower())


first=input("Enter firstname:")
print(first)
print(len(first))