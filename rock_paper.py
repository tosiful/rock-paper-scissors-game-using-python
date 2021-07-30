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


import random

img=[rock,paper,scissors]

human=int(input("what you chosise: "))
print(img[human])
computer= random.randint(0, 2)
print(img[computer])

if human >= 3 or human < 0:
  print("invalid")
elif human==0 and computer==2:
  print("human win")  
elif human==1 and computer==2:
  print("human win")
elif human==2 and computer==1:
  print("human win")
elif human==computer:
  print("draw")  
else:
  print("computer win") 



