#it is my 12th python project
#here i will print "i love you" with star pattern.


#it will print "i" 
for row in range (5):
    for col in range (4):
        if (row== 0 and col!= 0) or (row==1 and col==2) or (row==2 and col==2 ) or (row== 3 and col!= 0):
            print("*" , end= " ")
        else:
            print (end="  ")
    print()

#it will print heart shape
for row in range(6):
    for col in range(7):
        if (row== 0 and col%3 != 0) or (row== 1 and col%3 == 0 ) or (row-col==2) or (row+col == 8):
            print ("*" , end = " ")
        else :
            print ("  " , end="")
    print()

#it will print "U" shape 
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4)and row!= 6) or (row ==6 and (col!=0 and col!=4)):
            print ("*" , end=" ")
        else:
            print (end="  ")
    print()




