#Висилица
import random
def sozdanieV():
   HANGMAN_PICS = ['''
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
     ===''','''
  +---+
 [0   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
[/|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
[/|\] |
 / \  |
     ===''']
   return HANGMAN_PICS

world={'животные':'медведь баран волк лиса слон леопард пингвин павлин додо носорог коза коршун еж корова лось олень бык утка жираф кабан панда фламинго свинья обезьяна '.split(),
'фигуры':'квадрат треугольник паралелограм круг прямоугольник овал ромб трапеция шестиугольник'.split(),
'цвета':'красный оранжевый желтый зеленый голубой синий фазан'.split(),
'фрукты':'апельсин абрикос ананас арбуз дыня яблоко груша грейфрут лимон мандарин виноград '.split()}

def getRandomWorld(worldlist):
   wordkey = random.choice(list(worldlist.keys()))

   worldIndex = random.randint(0,len(worldlist[wordkey])-1)
   return [worldlist[wordkey][worldIndex],wordkey]

def funk(erorB,yB,sicretS,hang):
   print(hang[len(erorB)])
   print()
   
   print('Ошибачные буквы:',end=' ')
   for buk in erorB:
      print(buk,end=' ')

   print()

   leter = '_'*len(sicretS)

   for i in range(len(sicretS)):
      if sicretS[i] in yB:
          leter = leter[:i]+sicretS[i]+leter[i+1:]

   for letter in leter:
      print(letter, end = ' ')
   print()
   
def getGuess(alreadyGuessed):
   while True:
      print("Введите букву.")
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
         print('Введите одну букву.')
      elif guess in alreadyGuessed:
         print('Вы называли эту букву.Назовите другую.')
      elif guess not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
         print('Введите БУКВУ.')
      else:
         return guess

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

def vibor():
   print('Выберите уровень сложности.(Л,С,Т).')
   while True:
      otvet = input().upper()
      if len(otvet) !=1:
         print('Введите одну букву')
      elif otvet not in 'ЛСТ':
         print('Введите Л, С или Т')
      else:
         return otvet

def delVis(vybs,hangP):
   if vybs == 'С':
      del hangP[10]
      del hangP[9]
   if vybs == 'Т':
      del hangP[10]
      del hangP[9]
      del hangP[8]
      del hangP[7]

delV = True
errorB = ""
yesB = ""
gameOver = False
sicretS,keywords = getRandomWorld(world)

while True:
   if delV:
      hm = sozdanieV()

      bS = vibor()
      delVis(bS,hm)
      delV = False

   if bS == 'Л':
      print('Категория слова: '+keywords)
   funk(errorB,yesB,sicretS,hm)

   bukva = getGuess(errorB+yesB)

   if bukva in sicretS:
      yesB = yesB + bukva
      
      ssYes = True
      for i in range(len(sicretS)):
         if sicretS[i] not in yesB:
             ssYes = False
             break
      if ssYes:
          print('Да! Секретное слово - "'+sicretS+'"! Вы угадали!')
          gameOver = True
   else:
      errorB = errorB + bukva
      if len(errorB) == len(hm) -1:
         funk(errorB,yesB,sicretS, hm)
         print('Вы исчерпали все попытки!\nНеугадано букв '+str(len(errorB))+'\nУгадано букв '+str(len(yesB))+'\nЗагаданное слово '+str(sicretS))
         gameOver = True

   if gameOver:
      if playAgaiun():
         errorB = ''
         yesB = ''
         gameOver = False
         sicretS,keywords = getRandomWorld(world)
         delV = True
      else:
         break