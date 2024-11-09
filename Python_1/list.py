'''marks=[94,95.87,76,66,45]
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])


student=["Karan",94,22,"Gorakhpur"]
print(student[0])
student[0]="Omkar"
print(student)


#List Slicing
#list_name[start_index:ending_index]
marks=[96,74,85,77,55,66]
print(marks[:5])
print(marks[1:4])
print(marks[1:])
print(marks[-5:])
print(marks[-3:-1])

'''
#List Method
'''list=[2,1,3,4]
#append
list.append(5)
print(list)
#sort
print(list.sort())
print(list)

print(list.reverse())
print(list)

print(list.sort(reverse=True))
print(list)
'''
list1=["Apple","Banana","mango","litchi"]
#print(list1.sort(reverse=True))
#print(list1)

#print(list1.reverse)
#print(list1)

#print(list1.insert(3,"Gauva"))
#print(list1)

print(list1.pop(0))
print(list1)

print(list1.remove())