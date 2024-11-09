#Dictionary are unordered,mutable,do not allow duplicte key(means do value same nhi ho sakte hai)
'''
info={
    "key":"value",
    "name":"Omkar",
    "Age":21,
    "Gender":"Male",
    "subject":["DAA","DT","DA"],
    "marks":(45,85,98)
}
print(info)
print(info["name"])
print(info["marks"])
#mutable
info["name"]="Mahima"
info["surname"]="Singh"
print(info)
#creating null dictionary
null_dict={}
null_dict["name"]="Omkar"
print(null_dict)
#list and tuple are also stored in dictionary



#Nested Dictionary
student={
    "name":"Omkar",
    "subject":{
        "DAA":25,
        "DT":28,
        "BIDV":24,
        "COI":24,
    }
}
print(student)

#dictionary method
#1.dict.keys()
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
#2.dict.values()
print(student.values())
print(list(student.values()))
#3.dict.items()
print(student.items())
print(list(student.items()))
#4.dict.update(newdict)
new_dict={"city":"greaternoida"}
student.update(new_dict)
print(student)

#5.dict.get("key")
print(student.get("name"))

'''
#WAP to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and add one by one.Use subject name as key and marks as value.
marks={}
x=int(input("Enter pHysics:-"))
marks.update({"physics":x})
y=int(input("Enter math:-"))
marks.update({"math":y})
z=int(input("Enter chemistry:-"))
marks.update({"chemistry":z})
print(marks)