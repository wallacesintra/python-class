# tuple
# constructor tuple()
# ordered
# immutable
# enclosed by ()
# slicing - extract element using index
# allows duplication

# tuple() - constructor
# len() - no of element
# max()/min()
# sorted()
# sum()


# Q1 : height of plants in a garden as recorded in a survey
# enter the no. of 
n = eval(input("Enter the number of plants: "))
# read the height for each plant and store in a tuple
t = tuple() # storage
for i in range (n):
    height = eval(input("enter height at : "+str(i) + "\n"))
    t = t +(height,)

# display the height of each plant
print(t)
# display mean height
mean = sum(t)/len(t)
print('mean height is ', mean)
# display height for the tallest
print("tallest plant", max(t))
# standard deviation
z = 0.0
for i in range(len(t)):
    z = z + (t[i] - mean)**2
standardDeviation = (z/n)**0.5
print("the standard deviation : ", standardDeviation)
# the variance
print("the variance :", standardDeviation**2)
