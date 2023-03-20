# Functions
# a named re-usable piece of code that perform some tasks when called
# function Name(parameters : parameter list) return type
        #   body
# end function

# function add (PARAMETERS: x,y) return integer:
#      declare sum : integer
    #    calculate: = x+y
#         return sum
# end function

# function read(PARAMETER: none) RETURNS VOID
#        DECLARE a : integer
#        DECLARE b: integer
#        prompt for input of a and b
#        read a and b
#        CALL add(ARGUMENTS:a,b)
# end function

# def functionName(parameters-optional):
#      body
#      return statement- optional
     
def add(x,y):
    sum = x+y
    return sum
# calling function, invoking - include argument(s)
# functionName(arguments)
def get():
    a =eval(input("enter first no :"))
    b =eval(input("enter second no :"))
    print("the sum is {0}".format(add(a,b)))

get()    #call function

# example :develop a program that has two functions, the first prompt the user to input unique numbers that indentifies 
# students and store in a set then pass the set to a second function, the second function prompts the user to key in 
# reg.no then look for a match. If the no exists the function displays student registered otherwise displays 
# student not registered. this second function will to execute as long as the value is zero