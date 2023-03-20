#Dictionary -  a collection of unordered and mutable items enclosed by { }
# each item is described by a pair of properties (key&value) separated by :
# keys cant be duplicated

# properties
# order - unordered(cannt iterate)
# mutability - mutable
# heterogenus
# duplication - values can be duplicated but keys cannt
# slicing - no

# operations
# dict() - constructor
# clear() - remove all --- dictionaryName.clear()
# get() - return the value of the key  --- dictionaryName.get(key)
# len( ) return length 2 --- len(dictionaryName)
# zip() - concatenate keys and values
# values() - return sets of dictionary values ---- dictionaryName.value()
# keys() - return set of dictionary keys
# items() - return set of dictionary items --- dictionaryName.items()


# Example : dictionary name and no, perform 
# (i) display students details
list1 = list()
list2 = list()
d = dict()
no = eval(input("enter no of students : "))
for i in range(no):
    k = input("enter key at :" + str(i) + "\n")
    list1.append(k)
    v = input("enter value at "+ str(i) +"\n")
    list2.append(k)
d = dict(zip(list1,list2)) 
print("students :", d)   
# (ii) display all registration no.
print("student registration no. :", d.keys())
# (iii) display student names.
print("Student Names: ", d.values())
# (iv) given a reg.no locate the reg.no & student if they exist in the dictionary
x = input("enter key to search : ")
if x in d :
    print(x, str(":") + d[x])