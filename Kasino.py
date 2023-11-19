
from kRules import slot
from decouple import config


bank=int(config('MY_MONEY'))
while True:

   mybid = int(input('Ваша ставка ='))
   mynum = int(input('Вашe число ='))
   bank=slot(mynum,mybid,bank)   
   print(f'Ваш банк={bank}')
   answer = input("Вы хотите выйти? Да/Нет")
   if answer == "Да"or "да":
      print(f'Итог игры {bank}')
      break



