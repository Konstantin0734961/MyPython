#Висилица
from operator import iadd
import random
HANGMAN_PICS =['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  0   |
      |
      |
     ===''','''
  +---+
  0   |
  |   |
      |
     ===''','''
  +---+
  0   |
 /|   |
      |
     ===''','''
  +---+
  0   |
 /|\  |
      |
     ===''','''
  +---+
  0   |
 /|\  |
 /    |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']
world='медведь баран волк лиса слон леопард пингвин павлин додо носорог коза коршун еж корова сало лось олень бык утка жираф кабан панда '.split()
def getRandomWorld(worldlist):
   worldIndex = random.randint(0,len(worldlist)-1)
   return worldlist[worldIndex]

def funk(erorB,yB,sicretS):
   print(HANGMAN_PICS[len(erorB)])
   print()
   
   print('Ошибачные буквы:',end=' ')
   for buk in erorB:
      print(buk,end=' ')

   print()

   leter = '_'*len(sicretS)

   for i in range(len(sicretS)):
      if sicretS[i] in yB:
         leter = leter[:i]+sicretS[i]+leter[i+1:]

   print(leter)

def getGuess(alreadyGuessed):
   while True:
      print("Введите букву.")


erB = 'алку'
yesB = 'о'
siS = 'ворон'

funk(erB,yesB,siS)

def playAgaiun():
   print("Хотите сыграть ещё раз? (да или нет).")
   while True:
      otvet = input().lower()
      if (otvet == "да") or (otvet == "д") or (otvet == "yes") or (otvet =="y"):
         return True
      elif (otvet == "нет") or (otvet == "н") or (otvet == "no") or (otvet =="n"):
         return False
      else:
         print ("Ещё раз")

if playAgaiun():
   print("Игра продолжается")
else:
   print("Игра заканчивается")

errorB = ""
yesB = ""
gameOver = False
sicretS = getRandomWorld(worlds)

while True:
   displayBoard(errorB,yesB,sicretS)

   bukva = getGuess(errorB+yesB)

   if bukva in sicretS
      yesB = yesB + bukva
      if