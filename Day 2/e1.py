#if statement 

num1 = int(input("Type a number:  "))

is_even = False 
is_eight = False

if num1 % 2 == 0:
   # print(f"{num1} is even")
    is_even = True
    if num1 == 8:
        is_eight = True
    elif num1 == 4:
        pass

if is_even: #== True:
    print(f"{num1} is even")
    if is_eight:
        print(" num1 = 8")
elif is_even == False:
        print(f"{num1} is odd") 
    


