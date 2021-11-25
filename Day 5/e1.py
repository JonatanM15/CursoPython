import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list1 = [rock,paper,scissors]

choice = int(input("Make a choice 0-Rock, 1-Paper, 2-Scissors:  "))
computer = random.randint(0,2)

if choice > computer:
    print("User wins")

elif choice < computer :
    print("Computer wins")

elif choice == computer :
    print("It is a tie")

print("user")
print(list1[choice])
print("computer")
print(list1[computer])
