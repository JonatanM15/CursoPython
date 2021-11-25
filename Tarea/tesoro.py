print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")

if input("left o rigth: ").lower() == 'left':
    if input("swim or wait? : ").lower() == 'wait':
        color = "Wich door?: ".lower()
        if color == "yellow":
            print("you win")
        elif color == "blue":
            print("esaten by beasts")
        elif color == "red" :
            print("burned by fire")
        else:
            print("Game over")
    else:
        print("attacked by trout")
else: 
    print("Fall into a hole ")
