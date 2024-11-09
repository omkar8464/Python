tup=(2,4,6,7,8)
print(tup)
print(type(tup))
#Tuple mei value change nhi hoti hai ya fir alga se value add nhi kar sakte hai
#tup[0]=5
#empty tuple
tup=()
print(tup)
#Creating a singe tuple
tup=(1,)
print(tup)


tup=("hello","world")
print()

#Silicing in Tuple
tup=(1,2,3,4)
print(tup[1:3])


#Tuple Method
#tup.index(1)
#tup.count(1)
tup=(2,1,3,1,4,1)
print(tup.index(3))#find which place 3 is located at what index
print(tup.count(1))
