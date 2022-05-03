#word game with python

value = input("Do you want to play the game,type (yes/no)\n")

if value.lower().strip() == "yes":
    print("let's start")
    print("it is a adventure game")
    
    answer= input("Where do you want to go? (left/right)\n")
    if answer.lower().strip()== "left":
        print("you are going to left")
        
        answer= input("there is a sword,do you want to take it?(yes/no)\n")
        if answer.lower().strip()== "yes":
            print("great work,now you are going forward")
            print("opps! there is a monster")
            answer = input("do you want to attack? (yes/no) \n")
            if answer.lower().strip()=="yes":
                print("attack!")
                print("congrats you won the match")
                print("you got a golden egg")
                
            elif answer.lower().strip()=="no":
                print("monster killed you")
                print("sorry! game is over.....you died....")
                print("######################################")
                
            else:
                print("you are a coward")
                print("this game is over")
                
        elif answer.lower().strip()=="no":
            print("great work,now you are going forward")
            print("opps! there is a monster")
            answer = input("do you want to attack? (yes/no) \n")
            if answer.lower().strip()=="yes":
                print("attack!")
                print("monster is soo powerful,you can not hurt him with hand")
                print("sorry you lose the match")
                print("monster killed you")
                print("sorry! game is over.....you died....")
                print("######################################")
                
                
            elif answer.lower().strip()=="no":
                print("monster killed you")
                print("sorry! game is over.....you died....")
                print("######################################")

            else:
                print("you are a coward")
                print("this game is over")
        else:
            print("you typed wrong keyword....")
            print("plzz start the game again")   
    

    elif answer.lower().strip()=="right":
        print("you are going to right")
        
        answer = input ("there is a lighter,do you want to take it? (yes/no)\n")
        if  answer.lower().strip()== "yes":
            print("great work")
            print("you are going forword")
            answer=input("opp! there is a ghost!,Do you want to attack?(yes/no)\n")
            
            if  answer.lower().strip()== "yes":
                print("attack!")
                print("congrats you burned the ghost with lighter")
                print("you got a silver egg")
            elif  answer.lower().strip()=="no":
                print("Ghost killed you")
                print("game is over")
                
            else:
                print("Ghost killed you")
                print("game is over")
        
        elif answer.lower().strip()== "no":
            print("you are going forword")
            answer=input("opp! there is a ghost!,Do you want to attack?(yes/no)\n")
            
            if  answer.lower().strip()== "yes":
                print("attack!")
                print("ghost is too powerful you can not hurt him with your hand")
                print("Ghost killed you")
                print("game is over")

            elif  answer.lower().strip()=="no":
                print("Ghost killed you")
                print("game is over")
                
            else:
                print("Ghost killed you")
                print("game is over")
        
        else:
            print("you typed wrong keyword...")
            print("plzz start the game again")   
    
    else:
        print("that's way is not included in map")

else:
    print("You should play this game")
