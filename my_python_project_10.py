#it is my 10th python project
#here i am making "I" letter pattern

for row in range (5):
    for col in range (4):
        if (row== 0 and col!= 0) or (row==1 and col==2) or (row==2 and col==2 ) or (row== 3 and col!= 0):
            print("*" , end= " ")
        else:
            print (end="  ")
    print()


#it is my 14th python project
#here i am making "I" pattern

for row in range (5):
    for col in range (4):
        if (row== 0 and col!= 0) or (row==1 and col==2) or (row==2 and col==2 ) or (row== 3 and col!= 0):
            print("@" , end= " ")
        else:
            print (end="  ")
    print()
