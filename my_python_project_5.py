#IT is my 5th python project
#In this project i will make a currency coverter

currency1 = str(input ("type your currency "))
money  = int(input ("type your amount "))
currency2 = str(input ("type your sceond currency to convert "))

if currency1 == "tk" and currency2== "dollar":
    #here we are converting tk to dollar
    # 80tk = 1 dollar
    output = money/80
    print (output)
elif currency1== "dollar" and currency2 == "tk":
    #here we are converting dollar to tk
    # 1dollar = 80 tk
    output = money*80
    print (output)
elif currency1 == "euro" and currency2 == "tk":
    #here we are converting euro to tk
    # 1euro = 100tk
    output = money*100
    print (output)
elif currency1 == "tk" and currency2 == "euro":
    #here we are converting tk to euro
    #100tk = 1euro
    output = money/100
    print(output)
else:
    
    print("Go to the bank plzzzzz......")

