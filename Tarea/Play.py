"""path = str(input("Welcome to treasure island, Your mission is to find the treasure., You have to choose which way to take right or left : "))

next = False"""



print("Welcome to treasure island, tour mission is to find the treasure")

path =str(input("You have to choose left or right:  ")).lower()

keep = False

if path == "left" : 
 
    keep = True 
   
    print("You can go on")
else:
    print("Fall into a hole GAME OVER")
    quit()

sw =str(input("You want swim or wait: "))

keep = True
if sw == "swim" :