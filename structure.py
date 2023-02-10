#Sequence
# selection - Branch => if statement : single if
#                                     if...else
#                                     if ... elif...else
age = int(input("Enter the your age: "))

if age >= 1 and age < 18 :
    print ("Minor")
elif (age >= 18 and age< 35) :
    print("Youth")  
elif (age >= 35 and age< 65) :
    print("Adult") 
elif (age >= 65 and age< 120) :
    print("Youth") 
else : print("Invalid")        

#Loop : task is repeated 
#loop variable must be initiated, its value is updated after each iteration
# there is a condition to be tested, its either before or after
# to exit from the loop, break condition can be used, to skip task use continue
#            for i in range ():
#               do something

x = eval(input("enter the max value : "))
i = 1
for i in range(x): 
    print(i, end="\t")
    i+= 1