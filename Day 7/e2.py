import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword generator")
nr_letters = int(input("How many letters wold you like set your password?"))
nr_numbers = int(input("How many numbers wold you like set your password?"))
nr_simbols = int(input("How many simbols wold you like set your password?"))

password = ''
for char in range(1,nr_letters+1):
    #password = password + random.choice(letters)
    password += random.choice(letters)

for char in range(1,nr_numbers+1):
    password += random.choice(numbers)

for char in range(1,nr_simbols+1):
    password += random.choice(symbols)


#print(f"Passwor:  {password}")

password_list = []

for _ in range(1,nr_letters+1) :
    password_list.append(random.choice(letters))

for _ in range(1,nr_numbers+1) :
    password_list.append(random.choice(numbers))

for _ in range(1,nr_simbols) : 
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

final_password = ''
for element in password_list :
   # final_password = final_password + element
    final_password += element

print(final_password)
#print(password_list)


