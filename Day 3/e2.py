height = int(input("What is your height in cm: "))

can_ride = False

if height >= 120:
    can_ride = True
    #age < 12 --- $5
    #age <= 18 --- $7
    #age <= 45 --- $9
    #free 

if can_ride:
    age = int(input("How old are you?"))
    ticket = 0 
    if age < 12:
        #ticcket = ticket + 5
        ticket +=5 
       # print(f"you have to pay {ticket}")
    elif age <= 18:
        ticket += 7 
    elif age <= 45:
        ticket = 9
    elif age > 45:
        ticket = 0
    photo = input("Do you want a photo?:  (y/n)").lower()
    if photo == "y":
        ticket += 3
    print(f"you have to pay {ticket}")   

elif not can_ride: 
    print("you cannot ride")