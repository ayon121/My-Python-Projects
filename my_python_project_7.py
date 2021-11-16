#it is my 7th python project
#in this project i will  number pyramid

n = int(input ("type number"))

#first for loop use for row
for row in range(n):
    #2nd for is use for column 
    for col in range(row+1):
        print(col+1, end="")

    print()


#first for loop use for row
for row in range(n):
    #2nd for is use for column
    for col in range(n-row -1):
        print(col+1, end="")

    print()
#first for loop use for row
for row in range(n):
    #2nd for is use for column
    for col in range(row, -1 ,-1):
        print(col+1, end="")

    print()
