# set - unordered & immutable collection of elements enclosed by { }
# not sequential
# elements are immutable but the set is mutable
# no duplicate
# heterogenous

# operations
# set() - constructor
# add()- append item to the set --- setName.add(x)
# print() - output the set
# len() - return no of elements in a set ---- len(setName)
# discard() - remove element from the set --- setName discard(x)
# remove() - remove element from set --- setName(x), return error if no element
# union() - returns a collection of element in both sets --- setName1.union(setName2)
# intersection() -returns a collection of elements common in both sets --- s1.intersection (s2)
# difference() - returns element in minuend and not subtrahand --- s1.difference(s2)

# since a set is not ordered, one can create a list then pass it to the set

# example : write a program to record animals in two different farms then perform :
farm1 = set()
farm2 = set()
noFarm1 = eval(input("enter the no of animals in farm 1: "))
noFarm2 = eval(input("enter the no of animals in farm 2: "))

for i in range(noFarm1):
    x= input("enter name of animals in farm 1 :"+str(i) +"\n")
    farm1.add(x)

for i in range(noFarm2):
    y= input("enter name of animals in farm 2 :"+str(i) +"\n")
    farm2.add(y)   


# print animal in farm 1
print("animal in farm 1 :", farm1)

# print the animals in the 2 farms
print("animal in both farm", farm1.union(farm2))

# print common animals
print("common animal: ", farm1.intersection(farm2))

# print the animals that is in farm2 and not farm1
print(farm2.difference(farm1))