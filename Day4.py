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
list=[rock,paper,scissors]
print("Welcome you to this Game ")
human=int(input(" Enter your move Rock-->0 , paper--->1 , scissors--->2 \n"))
print(list[human])
randomValue=random.randint(0,2)
print(list[randomValue])
if human==randomValue:
    print("Draw")
elif human==0 and randomValue==1:
    print("computer WON")
elif human==1 and randomValue==2:
    print("computer won ")
elif human==3 and randomValue==1:
    print("computer won ")
else :
    print("you won")
