#Set is a collection of unordered items.
#Each element in the set must be uniqe and immutable.
"""collection={1,2,3,4,"hello","world"}
collection1={1,2,2,2,"hello","world"}
print(collection)
print(collection1)
print(type(collection))
print(len(collection1))

#creating empty set
coll=set()
print(coll)

#set method
#set.add(element)#adds an element
#set.remove(element)
#set.clear()#empties the set
#set.pop()#remove a random value

collection2=set()
collection2.add(1)
collection2.add(2)
collection2.add(2)
collection2.add(3)
collection2.remove(1)
collection2.clear()

print(collection2)

collection3={1,2,2,2,"hello","world"}
print(collection3.pop())

#union and intersection
set1={1,2,3,3,2}
set2={1,2,4,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))
"""

#Practice
#1.Store following word meanings in a python dictionary:
#a.table:"a piece of furniture","list of facts and figure"
#b.cat:"a small animal"
dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","list of fact and figure"],
}
print(dictionary)

#2.You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classroom are needed by all student.
#"python","java","C++","python","javascript","java","python","java","C++","C".
set3={
    "python","java","C++","python","javascript",
    "java","python","java","C++","C"
}
print(set3)
print(len(set3))

#Figure out a way to store 9 ans 9.0 as seperate value in the set.
values={9,9.0}
print(values)
