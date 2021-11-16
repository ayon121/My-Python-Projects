#my first python project
#it is a calculator

a = input ("give the first number: ")
b = input ("give the sceond number: ")
c = input ("give the operator ")

if c == "+" :
    x=a+b
    print ("it is summation")
elif c == "-" :
    x= a-b
    print ("it is minus")
elif c == "/" :
    x= a/b
    print ("it is division")
elif c == "*" :
    x= a*b
    print ("it is multiplication")
else:
    print ("wrong oparetor")
    print ("please try again")
print ( "total is"  , x)
