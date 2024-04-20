import random


while True:
    choice=["Rock","Papper","Sessor"]
    x=random.choice(choice)
    Gussed_Answer=input("Gussed Answer:")
    Gussed_Answer=Gussed_Answer.title()
    while Gussed_Answer not in choice:
            Gussed_Answer=input("Gussed Answer:")
            Gussed_Answer=Gussed_Answer.title()
    if x== Gussed_Answer:
        print("Actuall Answer:",x)
        print("Gussed Answer:",Gussed_Answer)
        print("Well Done")
        print("You Won")
    elif  x== "Rock":
        if Gussed_Answer == "Papper" :
            print("Actuall Answer:",x)
            print("Gussed Answer:",Gussed_Answer)
            print("Well Done")
            print("You Won")
        else:
            print("Actuall Answer:",x)
            print("Gussed Answer:",Gussed_Answer)
            print("Bad Luck")
            print("You Lose")
    elif  x== "Papper":
        if Gussed_Answer == "Rock":
            print("Actuall Answer:",x)
            print("Gussed Answer:",Gussed_Answer)
            print("Bad Luck")
            print("You Lose")
        else:
            print("Actuall Answer:",x)
            print("Gussed Answer:",Gussed_Answer)
            print("Well Done")
            print("You Won")   
    elif  x== "Sessor":
        if Gussed_Answer == "Rock":
            print("Actuall Answer:",x)
            print("Gussed Answer:",Gussed_Answer)
            print("Well Done")
            print("You Won") 
        else:
            print("Actuall Answer:",x)
            print("Gussed Answer:",Gussed_Answer)
            print("Bad Luck")
            print("You Lose")
    n=input("Enter q to quit and n to not")
    if n=="q":
        print("good bye")
        break

          
