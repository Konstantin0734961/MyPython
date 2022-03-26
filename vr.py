#Подключаем модуль
import random
attNumber = 0
myName = input("Здравствуйте! Как вас зовут?")
number = random.randint(1,20)
print("Что ж, "+myName+",я загадываю число от 1 до 20.")
for attNumber in range(6):
    print("Попробуй угадать.")
    guess = input()
    guess = int(guess)
    if guess < number:
        print("Твоё число слишком маленькое.")
    if guess > number:
        print("Твоё число слишком большое.")
    if guess == number:
        break
if guess == number:
    attNumber = str(attNumber + 1)
    print("Отлично, "+myName+"! Ты справился за "+attNumber+" попытки!")
if guess !=number:
    number = str(number)
    print("Увы. я загадал число "+number+".")